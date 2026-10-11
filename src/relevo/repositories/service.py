from uuid import UUID, uuid4

from relevo.database.sqlite import SQLite
from relevo.models.service import ServiceModel, ServiceStatus

class ServiceRepository:
  def __init__(self):
    self.db = SQLite()

  def create(
    self,
    name: str,
    account_id: UUID,
    status: ServiceStatus = ServiceStatus.ACTIVE,
  ) -> str:
    query = """
      INSERT INTO service (id, name, status, account_id)
      VALUES (%(id)s, %(name)s, %(status)s, %(account_id)s)
      RETURNING id;
    """

    params = {
      "id": str(uuid4()),
      "name": name,
      "status": status.value,
      "account_id": account_id,
    }
    results = self.db.query(sql=query, params=tuple(params.items()))
    if results:
      return results[0]["id"]

    raise Exception("Failed to create service")

  def find_by_id(self, id: UUID) -> ServiceModel | None:
    query = "SELECT * FROM service WHERE id = %(id)s"
    params = {"id": str(id)}
    results = self.db.query(sql=query, params=tuple(params.items()))
    if results:
      return ServiceModel.from_dict(results[0])
    return None

  def find_by_status(self, status: ServiceStatus) -> list[ServiceModel]:
    query = "SELECT * FROM service WHERE status = %(status)s"
    params = {"status": status.value}
    results = self.db.query(sql=query, params=tuple(params.items()))
    return [ServiceModel.from_dict(row) for row in results]

  def find_active(self) -> list[ServiceModel]:
    return self.find_by_status(ServiceStatus.ACTIVE)
