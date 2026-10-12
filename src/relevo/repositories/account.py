from uuid import uuid4

from relevo.database.sqlite import SQLite
from relevo.models.account import AccountModel, AccountStatus

class AccountRepository:
  def __init__(self):
    self.db = SQLite()

  def create(
    self,
    name: str,
    email: str,
    api_access_token: str,
    status: AccountStatus = AccountStatus.ACTIVE,
  ) -> str:
    query = """
      INSERT INTO accounts (id, name, email, status, api_access_token)
      VALUES (:id, :name, :email, :status, :api_access_token)
      RETURNING id;
    """

    params = {
      "id": str(uuid4()),
      "name": name,
      "email": email,
      "api_access_token": api_access_token,
      "status": status.value,
    }
    results = self.db.query(sql=query, params=params)
    if results:
      return results[0]["id"]

    raise Exception("Failed to create account")

  def find_by_id(self, id: str) -> AccountModel | None:
    query = "SELECT id, name, email, status, created_at, updated_at FROM accounts WHERE id = :id"
    params = {"id": id}
    results = self.db.query(sql=query, params=params)
    if results:
      return AccountModel.from_dict(results[0])
    return None

  def find_by_status(self, status: AccountStatus) -> list[AccountModel]:
    query = "SELECT id, name, email, status, created_at, updated_at FROM accounts WHERE status = :status"
    params = {"status": status.value}
    results = self.db.query(sql=query, params=params)
    return [AccountModel.from_dict(row) for row in results]

  def exists_by_id(self, id: str) -> bool:
    query = "SELECT 1 FROM accounts WHERE id = :id LIMIT 1"
    params = {"id": id}
    results = self.db.query(sql=query, params=params)
    return len(results) > 0
