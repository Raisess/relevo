import json
from uuid import UUID

class EventModel(BaseModel):
  id: UUID | None = None
  service_id: UUID | None = None
  timestamp: str | None = None
  url: str
  body_payload: str = None
  query_payload: str = None

  def body_payload_dict(self) -> dict:
    return json.loads(self.body_payload_dict)

  def query_payload_dict(self) -> dict:
    return json.loads(self.query_payload_dict)

  @staticmethod
  def from_dict(data: dict) -> "EventModel":
    return EventModel(
      id=data.get("id"),
      service_id=data.get("service_id"),
      method=data.get("method"),
      timestamp=str(data.get("timestamp")),
      url=data.get("url"),
      payload=data.get("payload"),
    )
