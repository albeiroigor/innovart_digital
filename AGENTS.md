# Innovart Digital — Flask REST API

Spanish-language ("mensaje", etc.) Flask API for Usuarios, Roles, Personas, Empleados, Servicios, Agenda, ServicioAgenda, Pagos, Consultas, Respuestas. Raw SQL via PyMySQL (no ORM, no migrations).

## Setup (do first, every time)

1. `cp .env.example .env` — `.env` is gitignored and does not exist in the repo; you must create it.
2. `.venv/` already exists: `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`).
3. `pip install -r requirements.txt` — Flask, PyMySQL, python-dotenv, Flask-Cors, gunicorn.
4. You need a running MySQL server (no SQLite fallback). Create the database named in `MYSQL_DATABASE` and set credentials in `.env`. Note: `Config.py` defaults the DB to `InnovartDigital`, while `.env.example` says `Innovartdb` — set `MYSQL_DATABASE` explicitly in `.env` to avoid a mismatch.

## Run

- `python app.py` — the real entrypoint (app factory `createApp()` in `app.py`). Reads `PORT` (default `5000`) and `FLASK_DEBUG` (set to `1` for debug mode).
- `run.py` exists but does `from App import app` (capital `A`), which fails on case-sensitive filesystems. Do not use it.
- Swagger UI: `http://127.0.0.1:5000/api/documentacion/`; raw spec: `/api/documentacion/swagger.json` (source: `swagger.json`, version 2.0.0, server `http://127.0.0.1:5000`).
- `/health` — verifica estado de la API y conexión a MySQL (`200` si OK, `503` si la BD está caída).

### Docker Compose

- `docker compose up -d` — levanta MySQL (`db`) y la API (`api`). Lee variables de `.env`.
- `docker compose logs -f api` — logs de la API.
- `docker compose down` — detiene; `docker compose down -v` también borra datos de MySQL.
- El `schema.sql` se monta en MySQL al iniciar y crea las tablas automáticamente.
- Dentro del contenedor, `MYSQL_HOST=db` (nombre del servicio, no `localhost`).

## Architecture (request flow)

`Routes/__init__.py` `loadRoutes(app)` registers all blueprints:

- `/api/usuarios` (UsuarioRoutes), `/api/roles`, `/api/personas`, `/api/empleados`, `/api/servicios`, `/api/servicios-agenda`, `/api/pagos`, `/api/consultas`, `/api/respuestas`
- Exception: `AgendaRoutes` mounts at `/agendas` (no `/api` prefix).
- `/api/documentacion` serves the Swagger UI.

Flow: Route (Flask Blueprint) -> `Controllers/*Controller.py` -> `Services/*Service.py` -> `Models/*.py` (data holder) -> `Database.MySQL` (pymysql, one lazy connection per request via Flask `g`, closed on teardown) -> MySQL. Services access the connection via `current_app.mysql.connection` (set in `app.py` as `app.mysql`).

## Database quirks

- Queries use mixed-case table names (`t_usuario`, `T_USUARIO`) — match exactly as written.
- Column `USU_CONTRASEÑA` contains `ñ`; passwords are hashed with `werkzeug.security` (`generate_password_hash` / `check_password_hash`).
- No migrations, no seed files, no test database.

## What does NOT exist here

- No `tests/` directory, no pytest, no lint/format/typecheck config, no CI workflows, no `ruff`/`mypy`/`flake8`. Do not invent test or lint commands; verify by running the API and hitting endpoints.

## Adding a new entity

Create `Models/X.py`, `Services/XService.py`, `Controllers/XController.py`, `Routes/XRoutes.py`, then register the blueprint with a `url_prefix` in `Routes/__init__.py` `loadRoutes(app)`.
