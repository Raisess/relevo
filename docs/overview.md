# Relevo - Project Structure

## Overall Architecture

Relevo is a Python-based webhook relay application built with **FastAPI**. The project follows a modular structure separating concerns into distinct layers:

```
relevo/
├── main.py           # App entry point - creates FastAPI instance with routers
├── __init__.py       # Package initialization
├── api/              # API routers (endpoints)
│   ├── health.py     # Health check routes
│   └── ingest.py     # Event ingestion routes
├── database/         # Data persistence layer
│   └── sqlite.py     # SQLite connection & query wrapper
├── migrations/       # SQL migration files for table creation
│   ├── 1791750837_accounts_table.sql  # accounts table with status index & email unique constraint
│   ├── 1791750843_services_table.sql # services table with FK to accounts & status indexes
│   └── 1791750848_events_table.sql   # events table with FK to services & service/url/timestamp indexes
├── models/           # Data domain models
│   ├── account.py    # Account entity with status enum
│   ├── event.py      # Event entity with payload parsing
│   └── service.py    # Service entity with status enum
├── repositories/     # Data repositories (CRUD operations)
│   ├── account.py    # AccountRepository
│   ├── event.py      # EventRepository
│   └── service.py    # ServiceRepository
└── docs/             # Documentation (this folder)
```

## How Components Connect

1. **Entry Point**: `main.py` creates the FastAPI app via `create_app()` and registers routers from `api/`

2. **API Layer**: Routes (`/health/ping`, `/ingest/{service_id}`) handle incoming requests

3. **Database Layer**: `database/sqlite.py` provides a `SQLite` class with `connect()`, `execute()`, and `query()` methods

4. **Models**: Data structures (`AccountModel`, `EventModel`, `ServiceModel`) define the domain entities. Factory methods (`from_dict()`) enable deserialization from database rows.

5. **Repositories**: Data access layer (`repositories/`) providing CRUD operations between API and database. Each repository class:
   - Holds a `SQLite` instance (`self.db`)
   - Takes connection path via `connect(path)`
   - Accepts model enums (`AccountStatus`, `ServiceStatus`) instead of raw integers for status parameters
   - Converts enum to `.value` when building SQL queries (SQLite stores integers)
   - Executes SQL queries
   - Returns model instances via `Model.from_dict()`

6. **Flow**: Incoming events via `/ingest/{service_id}` → API routes → Repositories → SQLite → Models

## Key Connection Flow

```
API Route → Repository (create/find) → SQLite query → Model.from_dict() → Domain object
```

- `main.py` includes `api/health.router` and `api/ingest.router` under `/health` and `/ingest` prefixes
- API routes can delegate to repositories for data persistence
- Repositories use `SQLite.connect()` before any database operations
- Models provide `from_dict()` to convert database row dicts to typed instances
- Empty space previously occupied by `controllers/` and now populated by `repositories/`