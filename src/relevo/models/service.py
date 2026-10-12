from dataclasses import dataclass
from enum import Enum

class ServiceStatus(Enum):
  INACTIVE = 0
  ACTIVE = 1


@dataclass
class ServiceModel:
  id: str
  created_at: str
  updated_at: str
  account_id: str
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
