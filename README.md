# DFIR event tracker

Shared catalog of digital-forensics conferences and summits (currently 2026–2027 editions).

**YAML is the only published catalog file.** This repository does not ship generated JSON. Consumers that must stay on the Python standard library convert the YAML in their own project, then cache JSON locally.

This repository does not fetch literature, compute upcoming/concluded status from today's date, or render a UI.

## How to contribute

Edit `events.yaml`.

- **`id` is immutable.** Do not rename an existing event id (`aafs-2026`, `dfrws-eu-2026`, …). Dashboards that pin of-interest items depend on it.
- Add an event with `id`, `name`, `series`, `start`, `end`, `city`, `location`, `format`, `url`, and optional `notes`.
- `start` and `end` are ISO dates (`YYYY-MM-DD`) or `null` when dates are not yet posted.
- `format` is `in-person`, `virtual`, or `hybrid`.
- Prefer official organizer pages for `url` and dates. Confirm before traveling; dates change.

Then run tests and open a pull request. Do not add a JSON file.

```bat
python -m pip install -r requirements-dev.txt
python -m pytest
```

## Repository layout

| File | Role |
| --- | --- |
| `events.yaml` | Edit this (source of truth) |
| `schema/events.schema.json` | Optional schema for the JSON consumers generate |
| `tests/` | Unique ids, required fields, and no published JSON |

## Using the catalog from another project

Copy or fetch `events.yaml`. Convert it to JSON **in that project** (PyYAML is only needed for the conversion step). Cache the JSON and keep a bundled snapshot for offline use; do not live-fetch GitHub on every page load.

Default raw URL:

`https://raw.githubusercontent.com/jgrover/dfir_event_tracker/main/events.yaml`

Derived fields such as `year`, `when`, `status`, and `upcoming` belong in the consumer, computed from today's date.

## License

MIT
