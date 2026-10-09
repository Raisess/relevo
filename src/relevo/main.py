from fastapi import FastAPI, APIRouter

from relevo.api.health import router as health_router

def create_app(routers: list[APIRouter]) -> FastAPI:
  app = FastAPI(title="Relevo")

  for router in routers:
    app.include_router(router)

  return app


app = create_app(routers=[health_router])
