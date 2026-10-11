# Database - Project Structure

The `database/` layer provides SQLite persistence for the Relevo application.

**Core Component:**
- `sqlite.py` — Contains the `SQLite` class and `SQLiteNotConnectedException` exception

**Connection Flow:**
1. Call `SQLite.connect(path="database.db")` to establish a connection
2. The connection is stored as `SQLite.connection` (class-level attribute)
3. All subsequent queries use `db.query(sql, params)` or `db.execute(sql, params)`
4. If `SQLite.connection` is `None`, `SQLiteNotConnectedException` is raised

**Methods:**
- `connect(path)` — Opens the SQLite database file
- `execute(sql, params)` — Runs INSERT/UPDATE/DELETE; auto-commits
- `query(sql, params)` — Runs SELECT; returns list of dicts (thanks to `__dict_factory`)

**Note:** The database layer is standalone; the app must explicitly connect before use. No automatic connection management or ORM is used.