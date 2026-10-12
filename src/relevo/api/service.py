from fastapi import APIRouter, Body, Header, HTTPException, status
from pydantic import BaseModel

from relevo.api.middleware import ACCESS_TOKEN_HEADER, validate_access_token
from relevo.controllers.service import ServiceController

router = APIRouter(prefix="/service")
controller = ServiceController()

class ServiceCreateSchema(BaseModel):
  name: str
  account_id: str
  status: int = 1


@router.post("/")
def create(
  data: ServiceCreateSchema = Body(...),
  x_access_token: str = Header(alias=ACCESS_TOKEN_HEADER),
):
  """Create a new service. Requires valid x-access-token header."""
  try:
    validate_access_token({"x-access-token": x_access_token})
  except ValueError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid or missing access token",
    )

  return controller.create(name=data.name, account_id=data.account_id, status=data.status)


@router.get("/")
def list_all(
  account_id: str | None = None,
  x_access_token: str = Header(alias=ACCESS_TOKEN_HEADER),
):
  """List services, optionally filtered by account. Requires valid x-access-token header."""
  try:
    validate_access_token({"x-access-token": x_access_token})
  except ValueError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid or missing access token",
    )

  if account_id:
    return controller.find_by_account_id(account_id)
  return controller.find_by_status()


@router.get("/{service_id}")
def get_by_id(
  service_id: str,
  x_access_token: str = Header(alias=ACCESS_TOKEN_HEADER),
):
  """Get service by ID. Requires valid x-access-token header."""
  try:
    validate_access_token({"x-access-token": x_access_token})
  except ValueError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid or missing access token",
    )

  return controller.find_by_id(service_id)