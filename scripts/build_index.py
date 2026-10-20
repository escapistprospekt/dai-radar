#!/usr/bin/env python3
"""
Regenerate index.json from the markdown source of truth in systems/ and
foundations/. Run this after any edit to those files. No dependencies
beyond the standard library.

Schema (index.json):
{
  "generated_at": "<ISO8601>",
  "systems": [
    {
      "path": "systems/ezkl.md",
      "frontmatter": {"name": "...", "field": "...", ...},
      "sections": {
        "What it does": {"markdown": "..."},
        "Property matrix": {"markdown": "...", "table": [{"Property": ..., "Value": ..., "Source": ...}, ...]},
        "Known limitations": {"markdown": "...", "list": ["...", "..."]},
        ...
      }
    },
    ...
  ],
  "foundations": [ same shape as systems ],
  "fields": [
    {"field": "ZKML / verifiable inference", "system": "systems/ezkl.md", "foundation": "foundations/zkml.md"}
    ...
  ]
}
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw_fm = text[3:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")
    fm: dict[str, str] = {}
    for line in raw_fm.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"')
        fm[key] = value
    return fm, body


def parse_table(block: str):
    rows = [l.strip() for l in block.splitlines() if l.strip().startswith("|")]
    if len(rows) < 2:
        return None
    header = [c.strip() for c in rows[0].strip("|").split("|")]
    data_rows = [r for r in rows[1:] if not re.match(r"^\|?\s*-+\s*(\|\s*-+\s*)*\|?$", r)]
    out = []
    for r in data_rows:
        cells = [c.strip() for c in r.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        out.append(dict(zip(header, cells)))
    return out or None


def parse_list(block: str):
    items = []
    current = None
    for line in block.splitlines():
        if re.match(r"^\s*-\s+", line):
            if current is not None:
                items.append(current.strip())
            current = re.sub(r"^\s*-\s+", "", line)
        elif current is not None and line.strip():
            current += " " + line.strip()
    if current is not None:
        items.append(current.strip())
    return items or None


def parse_sections(body: str) -> dict:
    # Drop a leading H1 title line if present.
    body = re.sub(r"^#\s+.*\n+", "", body, count=1)
    parts = re.split(r"^##\s+(.*)$", body, flags=re.MULTILINE)
    sections = {}
    # parts[0] is any preamble before the first ## heading; skip it.
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""
        entry = {"markdown": content}
        table = parse_table(content)
        if table:
            entry["table"] = table
        else:
            lst = parse_list(content)
            if lst:
                entry["list"] = lst
        sections[heading] = entry
    return sections


def load_dir(dirname: str):
    out = []
    for path in sorted((ROOT / dirname).glob("*.md")):
        text = path.read_text()
        fm, body = parse_frontmatter(text)
        out.append(
            {
                "path": f"{dirname}/{path.name}",
                "frontmatter": fm,
                "sections": parse_sections(body),
            }
        )
    return out


def main():
    systems = load_dir("systems")
    foundations = load_dir("foundations")
    watch_log = load_dir("watch/log")
    watch_log.sort(key=lambda w: w["frontmatter"].get("date", ""), reverse=True)

    checkpoint_path = ROOT / "watch" / "checkpoint.json"
    checkpoint = json.loads(checkpoint_path.read_text()) if checkpoint_path.exists() else None

    foundation_paths = {f["path"] for f in foundations}
    fields = []
    for s in systems:
        field = s["frontmatter"].get("field")
        # The system's own "foundation:" frontmatter is authoritative. Multiple
        # systems can share a field while citing different lineages (or none),
        # so this must never be inferred from the field name alone.
        foundation = s["frontmatter"].get("foundation")
        if foundation and foundation not in foundation_paths:
            print(f"WARNING: {s['path']} points to missing foundation '{foundation}'")
            foundation = None
        fields.append(
            {
                "field": field,
                "system": s["path"],
                "foundation": foundation,
            }
        )

    index = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "systems": systems,
        "foundations": foundations,
        "fields": fields,
        "watch_log": watch_log,
        "checkpoint": checkpoint,
    }

    out_path = ROOT / "index.json"
    out_path.write_text(json.dumps(index, indent=2) + "\n")
    print(f"wrote {out_path} ({len(systems)} systems, {len(foundations)} foundations)")


if __name__ == "__main__":
    sys.exit(main())
