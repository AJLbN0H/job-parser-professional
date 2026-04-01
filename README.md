# Job Parser Professional

Python console app for **job vacancy search and local cataloging**: it talks to the public **HeadHunter (hh.ru) API** (`requests`), normalizes vacancy fields (id, title, salary, requirements, URL), stores them in **`vacancies.json`**, and drives everything through an interactive **menu** (search API vs file, filter by ID or keyword, top-N by salary with optional range, manual add, clear file). The codebase uses small **OOP** layers (`API`, `FileWork`, `Vacancy`). Tests **mock HTTP** so CI stays deterministic without calling hh.ru.

![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![Requests](https://img.shields.io/badge/requests-HTTP-3182CE.svg)
![Poetry](https://img.shields.io/badge/poetry-managed-41454A.svg)
![Pytest](https://img.shields.io/badge/tests-pytest-orange.svg)
[![Tests](https://github.com/AJLbN0H/job-parser-professional/actions/workflows/tests.yml/badge.svg)](https://github.com/AJLbN0H/job-parser-professional/actions/workflows/tests.yml)

## Features

- **HeadHunter search** — `HeadHunterAPI.get_vacancies(keyword, per_page)` calls `https://api.hh.ru/vacancies`, maps salary (`from` / `to` → single number where applicable), and returns a list of dicts ready for JSON or display.
- **JSON storage** — `WorkingWithJSON` appends, reads, deletes selected rows, and clears `vacancies.json` (created on first use if missing).
- **Interactive menu** — `user_interaction()` in `src/main.py` guides search-in-API, search-in-file (by 9-digit ID or tokenized title match), top vacancies by salary, manual vacancy entry, and file reset.
- **Display helpers** — `src/utils.py` formats counts, ranges, sorted “top” lists, and optional delete prompts after a file search.
- **Tests** — `pytest` suite mocks `requests` and `api_vacancies.get_vacancies` so flows do not depend on network or live vacancy IDs.

## Stack

| Layer        | Technology                                      |
| ------------ | ----------------------------------------------- |
| HTTP         | Requests                                        |
| Data on disk | JSON (`vacancies.json`, UTF-8)                  |
| Packaging    | Poetry (`pyproject.toml` / `poetry.lock`)       |
| Tests        | Pytest (+ `pytest-cov` in **dev** group)      |
| Lint / types | Black, Flake8, isort, Mypy (**lint** group)     |

## Project layout

- `src/main.py` — menu loop, wires API + `WorkingWithJSON` + `Vacancy`.
- `src/api.py` — abstract `API`, concrete `HeadHunterAPI` (`_connect_api`, `get_vacancies`).
- `src/vacancies.py` — `Vacancy` model (`to_dict`, validation-style helpers used in tests).
- `src/file_work.py` — abstract `FileWork`, `WorkingWithJSON` implementation.
- `src/utils.py` — terminal output and user-facing helpers (`display_*`, `deleted_option`).
- `tests/` — unit tests for API (mocked), file I/O, main flows (mocked API), utils, vacancies.
- `vacancies.json` — runtime data file (created when you save vacancies; safe to delete for a clean state).

## Quick start (Docker)

1. Clone the repo:

   ```bash
   git clone https://github.com/AJLbN0H/job-parser-professional.git
   cd job-parser-professional
   ```

2. Build and run with Docker:

   ```bash
   docker build -t job-parser .
   docker run -it -v ./data:/app/data job-parser
   ```

   Or use Docker Compose:

   ```bash
   docker-compose up job-parser
   ```

> **Network:** live menu option "search via API" needs outbound HTTPS to hh.ru. Offline development is covered by tests with mocks.

## Tests (Docker)

```bash
docker run --rm job-parser python -m pytest -v
```

Or with Docker Compose:

```bash
docker-compose up job-parser-tests
```

## Local run with Poetry (alternative)

Install dependencies (the **dev** group includes Pytest):

```bash
poetry install --no-interaction --with dev
```

Run the console app:

```bash
poetry run python -m src.main
```

**Poetry + lockfile** is the supported path and matches CI.

## CI

GitHub Actions runs on pushes to **`main`** / **`develop`** and on pull requests targeting **`main`**: **Python 3.13**, `poetry install --no-interaction --no-root --with dev`, then `poetry run pytest`.

Workflow: [`.github/workflows/tests.yml`](.github/workflows/tests.yml).

## Roadmap

- Optional **CLI flags** or a thin Typer wrapper instead of a pure input-driven menu.
- **More boards** (SuperJob, Rabota.ru, etc.) behind the same `API` abstraction.
- **Exported `requirements.txt`** (or `pip-tools`) for environments without Poetry.
- Optional **marked integration tests** that hit hh.ru behind an env flag (skipped by default).
- **GUI or small web UI** (e.g. PyQt / FastAPI) on top of the same core modules.
