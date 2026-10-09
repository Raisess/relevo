from uuid import UUID

class ServiceModel:
  id: UUID | None = None
  created_at: str | None = None
  updated_at: str | None = None
  account_id: UUID | None = None
  name: str

  @staticmethod
  def from_dict(data: dict) -> "AccountModel":
    return AccountModel(
      id=d.get("id"),
      created_at=str(d.get("created_at")),
      updated_at=str(d.get("updated_at")),
      account_id=d.get("account_id"),
      name=d.get("name"),
    )
