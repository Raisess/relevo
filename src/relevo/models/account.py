from uuid import UUID

class AccountModel:
  id: UUID | None = None
  created_at: str | None = None
  updated_at: str | None = None
  name: str
  email: str

  @staticmethod
  def from_dict(data: dict) -> "AccountModel":
    return AccountModel(
      id=d.get("id"),
      created_at=str(d.get("created_at")),
      updated_at=str(d.get("updated_at")),
      name=d.get("name"),
      email=d.get("email"),
    )
