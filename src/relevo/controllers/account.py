from argon2 import PasswordHasher

from uuid import uuid4

from relevo.api.middleware import ACCESS_TOKEN_HEADER, validate_access_token
from relevo.controllers.exceptions.account import AccountNotFoundHttpException
from relevo.models.account import AccountModel, AccountStatus
from relevo.repositories.account import AccountRepository

class AccountController:
  def __init__(self, repository: AccountRepository | None = None):
    self.repository = repository or AccountRepository()

  def create(self, name: str, email: str, status: int = None) -> dict:
    api_access_token = str(uuid4())
    status = AccountStatus.ACTIVE if status == 1 or status == None else AccountStatus.INACTIVE

    password_hasher = PasswordHasher()
    id = self.repository.create(
      name=name,
      email=email,
      api_access_token=password_hasher.hash(api_access_token),
      status=status,
    )
    return { "id": id, "api_access_token": api_access_token }

  def find_by_id(self, id: str) -> AccountModel:
    account = self.repository.find_by_id(id)
    if not account:
      raise AccountNotFoundHttpException()

    return account

  def find_by_status(self, status: int = None) -> list[AccountModel]:
    status = AccountStatus.ACTIVE if status == 1 or status == None else AccountStatus.INACTIVE
    return self.repository.find_by_status(status)
