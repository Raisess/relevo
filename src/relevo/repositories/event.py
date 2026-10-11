import json
from uuid import UUID, uuid4

from relevo.database.sqlite import SQLite
from relevo.models.event import EventModel

class EventRepository:
  def __init__(self):
    self.db = SQLite()

  def create(
    self,
    service_id: UUID,
    url: str,
    body_payload: str | None = None,
    query_payload: str | None = None,
  ) -> str:
    query = """
      INSERT INTO event (id, service_id, url, body_payload, query_payload)
      VALUES (%(id)s, %(service_id)s, %(url)s, %(body_payload)s, %(query_payload)s)
      RETURNING id;
    """

    params = {
      "id": str(uuid4()),
      "service_id": str(service_id),
      "url": url,
      "body_payload": body_payload or "{}",
      "query_payload": query_payload or "{}",
    }
    results = self.db.query(sql=query, params=tuple(params.items()))
    if results:
      return results[0]["id"]

    raise Exception("Failed to create event")

  def find_by_service_id(self, service_id: UUID) -> list[EventModel]:
    query = "SELECT * FROM event WHERE service_id = %(service_id)s"
    params = {"service_id": str(service_id)}
    results = self.db.query(sql=query, params=tuple(params.items()))
    return [EventModel.from_dict(row) for row in results]

  def find_all(self) -> list[EventModel]:
    query = "SELECT * FROM event"
    results = self.db.query(sql=query, params=())
    return [EventModel.from_dict(row) for row in results]
