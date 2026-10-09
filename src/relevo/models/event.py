import json
from uuid import UUID

class EventModel(BaseModel):
  id: UUID | None = None
  timestamp: str | None = None
  url: str
  payload: str

  def payload_dict(self) -> dict:
    return json.loads(self.payload)

  @staticmethod
  def from_dict(data: dict) -> "EventModel":
    return AccountModel(
      id=d.get("id"),
      timestamp=str(d.get("timestamp")),
      url=d.get("url"),
      payload=d.get("payload"),
    )
