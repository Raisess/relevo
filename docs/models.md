# Models - Project Structure

The `models/` directory contains data domain models used across the Relevo application. These are plain Python classes that represent entity types and are used in conjunction with the repository layer for data persistence.

## Models Summary

| Model | File | Key Attributes |
|-------|------|----------------|
| `AccountModel` | `src/relevo/models/account.py` | `id`, `name`, `email`, `status` (AccountStatus enum) |
| `EventModel` | `src/relevo/models/event.py` | `id`, `service_id`, `url`, `body_payload`, `query_payload` |
| `ServiceModel` | `src/relevo/models/service.py` | `id`, `name`, `status` (ServiceStatus enum), `account_id` |

## Enums

- `AccountStatus`: `INACTIVE = 0`, `ACTIVE = 1`
- `ServiceStatus`: `INACTIVE = 0`, `ACTIVE = 1`

## Factory Methods

Each model provides a `from_dict(data: dict) -> ModelClass` static method that:

- Converts integer status values to the corresponding enum
- Maps dictionary keys to class attributes
- Enables deserialization from database rows or API payloads

### `AccountModel.from_dict(data: dict) -> AccountModel`

```python
account = AccountModel.from_dict({
    "id": uuid4(),
    "name": "Acme Corp",
    "email": "contact@acme.com",
    "status": 1,  # becomes AccountStatus.ACTIVE
})
```

### `ServiceModel.from_dict(data: dict) -> ServiceModel`

```python
service = ServiceModel.from_dict({
    "id": uuid4(),
    "name": "webhook-service",
    "status": 1,  # becomes ServiceStatus.ACTIVE
})
```

## Usage Pattern

```python
# From dictionary (e.g., database row)
account = AccountModel.from_dict({"id": uuid4(), "name": "Acme", "email": "a@b.com", "status": 1})

# Create with enum status
from relevo.models.account import AccountStatus
account = AccountModel.from_dict({"id": uuid4(), "name": "Acme", "email": "a@b.com", "status": AccountStatus.ACTIVE.value})
```