from relevo.controllers.exceptions.account import AccountNotFoundHttpException
from relevo.controllers.exceptions.service import ServiceNotFoundHttpException
from relevo.models.service import ServiceModel, ServiceStatus
from relevo.repositories.account import AccountRepository
from relevo.repositories.service import ServiceRepository

class ServiceController:
  def __init__(
    self,
    repository: ServiceRepository | None = None,
    account_repository: AccountRepository | None = None,
  ):
    self.repository = repository or ServiceRepository()
    self.account_repository = account_repository or AccountRepository()

  def create(self, name: str, account_id: str, status: int = None) -> dict:
    if not self.account_repository.exists_by_id_and_is_active(account_id):
      raise AccountNotFoundHttpException()

    status = ServiceStatus.ACTIVE if status == 1 or status == None else ServiceStatus.INACTIVE
    id = self.repository.create(name=name, account_id=account_id, status=status)
    return { "id": id }

  def find_by_id(self, id: str) -> ServiceModel:
    service = self.repository.find_by_id(id)
    if not service:
      raise ServiceNotFoundHttpException()

    return service

  def find_by_status(self, status: int = None) -> list[ServiceModel]:
    status = ServiceStatus.ACTIVE if status == 1 or status == None else ServiceStatus.INACTIVE
    return self.repository.find_by_status(status)

  def find_by_account_id(self, account_id: str) -> list[ServiceModel]:
    return self.repository.find_by_account_id(account_id)
