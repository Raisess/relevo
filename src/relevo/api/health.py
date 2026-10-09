from fastapi import APIRouter

router = APIRouter(prefix="/health")

@router.get("/ping")
def ping():
  return "pong"
