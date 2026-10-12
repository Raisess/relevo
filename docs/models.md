# Models - Project Structure

The `models/` directory contains data domain models used across the Relevo application. These are `@dataclass` classes that represent entity types and are used in conjunction with the repository layer for data persistence.

## Models Summary

| Model | File | Key Attributes |
|-------|------|----------------|
| `AccountModel` | `src/relevo/models/account.py` | `id`, `created_at`, `updated_at`, `name`, `email`, `status` (AccountStatus enum), `api_access_token` |
| `EventModel` | `src/relevo/models/event.py` | `id`, `service_id`, `timestamp`, `url`, `body_payload`, `query_payload` |
| `ServiceModel` | `src/relevo/models/service.py` | `id`, `created_at`, `updated_at`, `account_id`, `status` (ServiceStatus enum), `name` |

## Conventions

- Models are declared with Python's `@dataclass` decorator.
- Identifiers (`id`, `account_id`, `service_id`) are plain `str` — repositories serialize values on persistence, so no `UUID` conversion happens in this layer and the values are ready for the API return.
- Timestamps (`created_at`, `updated_at`, `timestamp`) are `str`.
- All fields are required (no defaults); dataclass default-ordering rules apply to field declarations.
- `status` is an enum in Python (`AccountStatus`/`ServiceStatus`) and is stored as an `INTEGER` (0 or 1) in SQLite.
- FastAPI serializes dataclass instances returned from routes directly (dataclass → dict, enum → value).

## Enums

- `AccountStatus`: `INACTIVE = 0`, `ACTIVE = 1`
- `ServiceStatus`: `INACTIVE = 0`, `ACTIVE = 1`

## Factory Methods

Each model provides a `from_dict(data: dict) -> ModelClass` static method that:

- Converts integer status values to the corresponding enum (`1` → `ACTIVE`, anything else → `INACTIVE`)
- Maps dictionary keys to dataclass fields
- Enables deserialization from database rows or API payloads

### `AccountModel.from_dict(data: dict) -> AccountModel`

```python
account = AccountModel.from_dict({
    "id": "0482c38a-f107-42b1-9259-fece7343cb97",
    "created_at": "2026-10-12 09:00:00",
    "updated_at": "2026-10-12 09:00:00",
    "name": "Acme Corp",
    "email": "contact@acme.com",
    "status": 1,  # becomes AccountStatus.ACTIVE
    "api_access_token": "0482c38a-f107-42b1-9259-fece7343cb97",
})
```

### `ServiceModel.from_dict(data: dict) -> ServiceModel`

```python
service = ServiceModel.from_dict({
    "id": "0482c38a-f107-42b1-9259-fece7343cb97",
    "created_at": "2026-10-12 09:00:00",
    "updated_at": "2026-10-12 09:00:00",
    "account_id": "1e312e93-1175-467d-83f9-1dcf80aa5251",
    "status": 1,  # becomes ServiceStatus.ACTIVE
    "name": "webhook-service",
})
```

## Usage Pattern

```python
# From dictionary (e.g., database row)
account = AccountModel.from_dict({
    "id": "0482c38a-f107-42b1-9259-fece7343cb97",
    "created_at": "2026-10-12 09:00:00",
    "updated_at": "2026-10-12 09:00:00",
    "name": "Acme",
    "email": "a@b.com",
    "status": 1,
    "api_access_token": "0482c38a-f107-42b1-9259-fece7343cb97",
})

# Status is kept as an enum on the model
from relevo.models.account import AccountStatus
assert account.status is AccountStatus.ACTIVE
```
