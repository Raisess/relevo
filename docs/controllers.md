# Controllers - Project Structure

The `controllers/` directory is currently **empty** and part of the project's modular structure.

**Role in Architecture:**
- Intended to handle HTTP request logic and business orchestration
- Would sit between API routes (`api/`) and data repositories (`repositories/`)
- Currently not implemented; API routes handle requests directly

**Connection Path (future):**
```
API route → Controller (business logic) → Repository (data access) → Database
```

**Current State:**
No controllers implemented. Routes in `api/` perform all request handling.