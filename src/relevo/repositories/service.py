from uuid import uuid4

from relevo.database.sqlite import SQLite
from relevo.models.service import ServiceModel, ServiceStatus

class ServiceRepository:
  def __init__(self):
    self.db = SQLite()

  def create(
    self,
    name: str,
    account_id: str,
    status: ServiceStatus = ServiceStatus.ACTIVE,
  ) -> str:
    query = """
      INSERT INTO services (id, name, status, account_id)
      VALUES (:id, :name, :status, :account_id)
      RETURNING id;
    """

    params = {
      "id": str(uuid4()),
      "name": name,
      "status": status.value,
      "account_id": account_id,
    }
    results = self.db.query(sql=query, params=params)
    if results:
      return results[0]["id"]

    raise Exception("Failed to create service")

  def find_by_id(self, id: str) -> ServiceModel | None:
    query = "SELECT * FROM services WHERE id = :id"
    params = {"id": id}
    results = self.db.query(sql=query, params=params)
    if results:
      return ServiceModel.from_dict(results[0])
    return None

  def find_by_status(self, status: ServiceStatus) -> list[ServiceModel]:
    query = "SELECT * FROM services WHERE status = :status"
    params = {"status": status.value}
    results = self.db.query(sql=query, params=params)
    return [ServiceModel.from_dict(row) for row in results]

  def find_active(self) -> list[ServiceModel]:
    return self.find_by_status(ServiceStatus.ACTIVE)

  def find_by_account_id(self, account_id: str) -> list[ServiceModel]:
    query = "SELECT * FROM services WHERE account_id = :account_id"
    params = {"account_id": account_id}
    results = self.db.query(sql=query, params=params)
    return [ServiceModel.from_dict(row) for row in results]
