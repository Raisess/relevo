# Repositories - Project Structure

The `repositories/` directory now implements the data access layer, following modular architecture patterns.

**Implemented Repositories:**

| Repository | File | Key Methods |
|------------|------|-------------|
| `AccountRepository` | `src/relevo/repositories/account.py` | `create()`, `find_by_id()`, `find_by_status()` |
| `EventRepository` | `src/relevo/repositories/event.py` | `create()`, `find_by_service_id()`, `find_all()` |
| `ServiceRepository` | `src/relevo/repositories/service.py` | `create()`, `find_by_id()`, `find_by_status()`, `find_active()` |

**Connection Pattern:**

```
Repository → SQLite database layer → Model instances via from_dict()
```

**Database Dependency:**
All repositories use `relevo.database.sqlite.SQLite` for persistence:
- Call `repository.connect(path="database.db")` to establish connection
- Accept model enums (`AccountStatus`, `ServiceStatus`) instead of raw integers for status parameters
- Convert enum to `.value` when building SQL queries (SQLite stores integers)
- All queries go through `self.db.query(sql, params)` or `self.db.execute(sql, params)`
- Results are converted to model instances via `Model.from_dict(row)`

**AccountRepository (`src/relevo/repositories/account.py`)**
- `create(name, email, status=AccountStatus.ACTIVE)` → inserts account, returns `AccountModel`
  - `status` accepts `AccountStatus.ACTIVE` or `AccountStatus.INACTIVE` (converted to `.value` for SQL)
- `find_by_id(id)` → returns `AccountModel` or `None`
- `find_by_status(status)` → returns list of `AccountModel` instances
  - `status` accepts `AccountStatus.ACTIVE` or `AccountStatus.INACTIVE`

**EventRepository (`src/relevo/repositories/event.py`)** 
- `create(service_id, url, body_payload, query_payload)` → inserts event, returns `EventModel`
- `find_by_service_id(service_id)` → returns list of `EventModel` instances
- `find_all()` → returns all `EventModel` instances

**ServiceRepository (`src/relevo/repositories/service.py`)**
- `create(name, status=ServiceStatus.ACTIVE, account_id=None)` → inserts service, returns `ServiceModel`
  - `status` accepts `ServiceStatus.ACTIVE` or `ServiceStatus.INACTIVE` (converted to `.value` for SQL)
- `find_by_id(id)` → returns `ServiceModel` or `None`
- `find_by_status(status)` → returns list of `ServiceModel` instances
  - `status` accepts `ServiceStatus.ACTIVE` or `ServiceStatus.INACTIVE`
- `find_active()` → convenience method for active services only

**Flow Example:**
```python
from relevo.repositories.sqlite import SQLite
from relevo.repositories.account import AccountRepository

SQLite.connect("database.db")
repo = AccountRepository()
account = repo.create(name="Acme", email="contact@acme.com")
found = repo.find_by_id(account.id)
```