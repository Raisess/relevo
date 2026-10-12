from typing import Annotated

from fastapi import APIRouter, Path, Request

router = APIRouter(prefix="/ingest")

@router.post("/{service_id}")
def ingest(
  service_id: Annotated[str, Path(title="A valid service id for the event to be registered.")],
  request: Request,
):
  return "pong"
