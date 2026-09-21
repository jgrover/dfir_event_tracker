from __future__ import annotations

from datetime import date
from pathlib import Path

from yaml_catalog import yaml_payload

ROOT = Path(__file__).resolve().parents[1]


def test_ids_are_unique_and_required() -> None:
    payload = yaml_payload()
    ids = [str(row["id"]) for row in payload["events"]]
    assert ids
    assert all(str(row.get("name") or "").strip() for row in payload["events"])
    assert len(ids) == len(set(ids))
    assert payload["version"] == 1
    assert len(payload["events"]) >= 20


def test_dates_are_iso_or_null() -> None:
    payload = yaml_payload()
    allowed_formats = {"in-person", "virtual", "hybrid", ""}
    for row in payload["events"]:
        for key in ("start", "end"):
            value = row.get(key)
            if value is None:
                continue
            if isinstance(value, date):
                continue
            parsed = date.fromisoformat(str(value))
            assert parsed.isoformat() == str(value)
        assert str(row.get("format") or "") in allowed_formats


def test_json_is_not_published() -> None:
    assert (ROOT / "events.yaml").is_file()
    assert not (ROOT / "events.json").exists()
