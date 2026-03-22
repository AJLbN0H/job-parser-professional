# Job Parser Professional

[![Tests](https://github.com/AJLbN0H/job-parser-professional/actions/workflows/tests.yml/badge.svg)](https://github.com/AJLbN0H/job-parser-professional/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Testing](https://img.shields.io/badge/pytest-enabled-brightgreen.svg)

Console utility for searching and managing job vacancies from the [HeadHunter (hh.ru) API](https://api.hh.ru/openapi/redoc). Vacancies can be stored locally in `vacancies.json`, filtered by keyword or ID, ranked by salary, and edited from the menu.

## Features

- **HeadHunter API:** Fetch vacancies by keyword and result count (up to 100 per request).
- **Local JSON storage:** Append, list, delete, and clear vacancies in `vacancies.json`.
- **CLI menu:** Search in API or in file, top-N by salary (optional salary range), manual vacancy entry, file reset.
- **Tests:** Unit tests with mocks for HTTP so CI does not depend on the live API.

## Tech stack

- Python 3.13+
- `requests` for HTTP
- `pytest`, `pytest-cov` for tests

## Project layout

| Path | Role |
|------|------|
| `src/main.py` | Interactive menu and user flow |
| `src/api.py` | Abstract API + `HeadHunterAPI` client |
| `src/vacancies.py` | `Vacancy` model |
| `src/file_work.py` | JSON file read/write helpers |
| `src/utils.py` | Display and helper functions |
| `tests/` | Pytest suite |

## Setup

Requires [Poetry](https://python-poetry.org/).

```bash
git clone https://github.com/AJLbN0H/job-parser-professional.git
cd job-parser-professional
poetry install
```

## Run

From the project root (with the virtualenv active):

```bash
poetry run python -m src.main
```

Or, after `poetry shell`:

```bash
python -m src.main
```

## Tests

```bash
poetry run pytest
```

Coverage example:

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

## CI

GitHub Actions workflow `.github/workflows/tests.yml` runs `pytest` on pushes to `main` / `develop` and on pull requests targeting `main`.

## Roadmap

- Additional job boards (SuperJob, Rabota.ru, etc.).
- Optional GUI (e.g. PyQt) or a small web UI (e.g. FastAPI).
- Async fetching for larger batches.
