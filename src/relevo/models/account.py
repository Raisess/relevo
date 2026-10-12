from dataclasses import dataclass
from enum import Enum

class AccountStatus(Enum):
  INACTIVE = 0
  ACTIVE = 1


@dataclass
class AccountModel:
  id: str
  created_at: str
  updated_at: str
  status: AccountStatus
  name: str
  email: str
  api_access_token: str

  @staticmethod
  def from_dict(data: dict) -> "AccountModel":
    status = AccountStatus.ACTIVE if data.get("status") == 1 else AccountStatus.INACTIVE

    return AccountModel(
      id=data.get("id"),
      created_at=str(data.get("created_at")),
      updated_at=str(data.get("updated_at")),
      name=data.get("name"),
      email=data.get("email"),
      api_access_token=data.get("api_access_token"),
      status=status,
    )
