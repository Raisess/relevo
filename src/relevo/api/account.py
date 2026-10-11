from fastapi import APIRouter, Body, Header, HTTPException, status
from pydantic import BaseModel

from relevo.api.middleware import ACCESS_TOKEN_HEADER, validate_access_token
from relevo.controllers.account import AccountController

router = APIRouter(prefix="/account")
controller = AccountController()

class AccountCreateSchema(BaseModel):
  name: str
  email: str
  status: int = 1


@router.post("/")
def create(
  data: AccountCreateSchema = Body(...),
  x_access_token: str = Header(alias=ACCESS_TOKEN_HEADER),
):
  """Create a new account. Requires valid x-access-token header."""
  try:
    validate_access_token({"x-access-token": x_access_token})
  except ValueError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid or missing access token",
    )

  account_status = AccountStatus(data.status) if data.status else AccountStatus.ACTIVE
  return controller.create(name=data.name, email=data.email, status=account_status)


@router.get("/")
def list_all(
  x_access_token: str = Header(alias=ACCESS_TOKEN_HEADER),
):
  """List all accounts. Requires valid x-access-token header."""
  try:
    validate_access_token({"x-access-token": x_access_token})
  except ValueError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid or missing access token",
    )

  from relevo.models.account import AccountStatus as AS
  return controller.find_by_status(AccountStatus.ACTIVE)


@router.get("/{account_id}")
def get_by_id(
  account_id: str,
  x_access_token: str = Header(alias=ACCESS_TOKEN_HEADER),
):
  """Get account by ID. Requires valid x-access-token header."""
  try:
    validate_access_token({"x-access-token": x_access_token})
  except ValueError:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid or missing access token",
    )

  return controller.find_by_id(account_id)
