from relevo.api.middleware import ACCESS_TOKEN_HEADER, validate_access_token
from relevo.models.account import AccountModel, AccountStatus
from relevo.repositories.account import AccountRepository

class AccountController:
  def __init__(self, repository: AccountRepository | None = None):
    self.repository = repository or AccountRepository()

  def create(self, name: str, email: str, status: int = None) -> AccountModel:
    status = AccountStatus.ACTIVE if status == 1 or status == None  else AccountStatus.INACTIVE
    return self.repository.create(name=name, email=email, status=status)

  def find_by_id(self, id: str) -> AccountModel | None:
    from uuid import UUID
    return self.repository.find_by_id(UUID(id))

  def find_by_status(self, status: int = None) -> list[AccountModel]:
    status = AccountStatus.ACTIVE if status == 1 or status == None else AccountStatus.INACTIVE
    return self.repository.find_by_status(status)
