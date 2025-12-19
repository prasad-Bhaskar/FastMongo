# Project Installation and Setup

This document shows how to set up and run the FastAPI + Mongo (Motor) project on Windows when your system Python is 3.13 but the project requires Python 3.11.

## Overview
- Project root contains `requirements.txt` with pinned dependencies.
- App entrypoint: `app.main:app` (run with `uvicorn`).
- Configuration is read from environment variables or a `.env` file via `app.core.config.Settings` (see required keys below).

## Prerequisites
- Internet access to download Python and packages.
- Admin or user permissions to install Python and create virtual environments.

## Required environment variables
This project expects these variables (or placed in a `.env` file at project root):

- `MONGO_URI` — MongoDB connection URI (e.g. `mongodb://user:pass@host:port`).
- `DB_NAME` — Database name used by the app.
- `JWT_SECRET` — Secret string used to sign JWT tokens.
- `JWT_ALGORITHM` — (optional) defaults to `HS256`.
- `ACCESS_TOKEN_EXPIRE_MINUTES` — (optional) defaults to `30`.

Example `.env` file (create a file named `.env` in the project root):

MONGO_URI="mongodb://localhost:27017"
DB_NAME="fastmongo"
JWT_SECRET="change-me-to-a-secret"
JWT_ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

> Keep secrets (like `JWT_SECRET`) out of version control. Use a secrets manager in production.

## Install Python 3.11 (Windows)
You have Python 3.13 installed, but the project is developed/tested against Python 3.11. Options:

Option A — Install Python 3.11 alongside 3.13 (recommended):
1. Download the official installer for Python 3.11 from https://www.python.org/downloads/release/python-3119/.
2. Run the installer and ensure you check "Add Python 3.11 to PATH" or note the install path.
3. You will then have a `python3.11` or `py -3.11` launcher available.

Option B — Use `pyenv-win` or `scoop` to install/manage multiple Python versions (advanced).

Option C — Use conda/miniconda/Anaconda and create a dedicated Python 3.11 environment.

## Recommended: Create a Python 3.11 virtual environment (PowerShell)
Replace `py -3.11` with the exact path or `py` launcher on your system if different.

1. From project root open PowerShell.
2. Create the venv:

```powershell
py -3.11 -m venv .venv
```

3. Activate the venv in PowerShell:

```powershell
.\.venv\Scripts\Activate
```

If PowerShell prevents running scripts, enable local activation for the current user (only if you understand the policy):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

4. Verify Python version inside the venv:

```powershell
python --version
# Should show Python 3.11.x
```

## Installing dependencies from `requirements.txt`
With the virtual environment activated, upgrade pip and install:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you prefer, create a reproducible, isolated environment with `pip-tools` or `venv` + `pip` is fine for development.

## Environment setup before running
1. Create `.env` file in project root (example above) or export environment variables.
2. Ensure your MongoDB server is reachable at `MONGO_URI` and the user has permissions.

## Running the application
With the virtualenv activated and dependencies installed:

```powershell
# From project root
uvicorn app.main:app --reload --port 8000
```

- The API docs will be available at `http://127.0.0.1:8000/docs`.

## Common notes and troubleshooting
- If `py -3.11` is not found, point to the explicit Python 3.11 executable (e.g. `C:\Python311\python.exe -m venv .venv`).
- If packages fail to install due to binary wheels, ensure you have a suitable C compiler or install pre-built wheels (Windows may require Build Tools).
- For MongoDB local installs, you can run a Docker container:

```powershell
docker run -d -p 27017:27017 --name mongo mongo:6
```

Then set `MONGO_URI=mongodb://localhost:27017`.

## Development helpers
- Run tests (if present) with `pytest` after installing dev dependencies.
- Lint or format with `flake8` / `black` if configured.

## Summary (Quick start)
1. Install Python 3.11 (if missing).
2. Create & activate venv:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install deps:

```powershell
pip install -r requirements.txt
```

4. Add `.env` with required keys.
5. Run app:

```powershell
uvicorn app.main:app --reload
```

---

If you want, I can also:
- Add a `pyproject.toml`/`dev-requirements.txt` for development tooling.
- Add a `Makefile` or `scripts` to ease venv creation on Windows.
- Add a sample `.env.example` file in the repo.

Let me know which additions you'd like and I can create them now.