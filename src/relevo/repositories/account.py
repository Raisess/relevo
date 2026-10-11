from uuid import UUID, uuid4

from relevo.database.sqlite import SQLite
from relevo.models.account import AccountModel, AccountStatus

class AccountRepository:
  def __init__(self):
    self.db = SQLite()

  def create(
    self,
    name: str,
    email: str,
    status: AccountStatus = AccountStatus.ACTIVE,
  ) -> str:
    query = """
      INSERT INTO account (id, name, email, status)
      VALUES (%(id)s, %(name)s, %(email)s, %(status)s)
      RETURNING id;
    """

    params = {"id": str(uuid4()), "name": name, "email": email, "status": status.value}
    results = self.db.query(sql=query, params=tuple(params.items()))
    if results:
      return results[0]["id"]

    raise Exception("Failed to create account")

  def find_by_id(self, id: UUID) -> AccountModel | None:
    query = "SELECT * FROM account WHERE id = %(id)s"
    params = {"id": str(id)}
    results = self.db.query(sql=query, params=tuple(params.items()))
    if results:
      return AccountModel.from_dict(results[0])
    return None

  def find_by_status(self, status: AccountStatus) -> list[AccountModel]:
    query = "SELECT * FROM account WHERE status = %(status)s"
    params = {"status": status.value}
    results = self.db.query(sql=query, params=tuple(params.items()))
    return [AccountModel.from_dict(row) for row in results]
