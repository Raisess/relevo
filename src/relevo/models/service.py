from enum import Enum
from uuid import UUID

class ServiceStatus(Enum):
  INACTIVE = 0
  ACTIVE = 1


class ServiceModel:
  id: UUID | None = None
  created_at: str | None = None
  updated_at: str | None = None
  account_id: UUID | None = None
  status: ServiceStatus
  name: str

  @staticmethod
  def from_dict(data: dict) -> "ServiceModel":
    status = ServiceStatus.ACTIVE if data.get("status") == 1 else ServiceStatus.INACTIVE

    return ServiceModel(
      id=data.get("id"),
      created_at=str(data.get("created_at")),
      updated_at=str(data.get("updated_at")),
      account_id=data.get("account_id"),
      name=data.get("name"),
      status=status,
    )
