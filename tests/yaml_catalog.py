from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def yaml_payload() -> dict:
    raw = yaml.safe_load((ROOT / "events.yaml").read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise TypeError("YAML root must be a mapping")
    events = []
    seen: set[str] = set()
    for row in raw.get("events") or []:
        if not isinstance(row, dict):
            continue
        eid = str(row.get("id") or "").strip()
        name = str(row.get("name") or "").strip()
        if not eid or not name:
            continue
        if eid in seen:
            raise ValueError(f"duplicate event id: {eid}")
        seen.add(eid)
        events.append(row)
    return {
        "version": int(raw.get("version") or 1),
        "events": events,
    }
