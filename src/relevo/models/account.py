from enum import Enum
from uuid import UUID

class AccountStatus(Enum):
  INACTIVE = 0
  ACTIVE = 1


class AccountModel:
  id: UUID | None = None
  created_at: str | None = None
  updated_at: str | None = None
  status: AccountStatus
  name: str
  email: str

  @staticmethod
  def from_dict(data: dict) -> "AccountModel":
    status = AccountStatus.ACTIVE if data.get("status") == 1 else AccountStatus.INACTIVE

    return AccountModel(
      id=data.get("id"),
      created_at=str(data.get("created_at")),
      updated_at=str(data.get("updated_at")),
      name=data.get("name"),
      email=data.get("email"),
      status=status,
    )
