from typing import Annotated

from fastapi import APIRouter, Body, Path, Query

router = APIRouter(prefix="/ingest")

# @TODO: get caller url from header
@router.post("/{service_id}")
def ingest(
  service_id: Annotated[str, Path(title="A valid service id for the event to be registered.")],
  query_payload: Annotated[dict, Query(title="The webhook event query payload.")],
  body_payload: Annotated[dict, Body(title="The webhook event body payload.")],
):
  return "pong"
