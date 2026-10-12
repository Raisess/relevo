import json
from dataclasses import dataclass

@dataclass
class EventModel:
  id: str
  service_id: str
  timestamp: str
  url: str
  body_payload: str | None = None
  query_payload: str | None = None

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
