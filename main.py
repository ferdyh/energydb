import uvicorn
import asyncio

from alembic.config import Config
from alembic import command

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.consolidator import Consolidator
from routers import meters

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(meters.router, prefix="/api")

def run_migrations(script_location: str, dsn: str) -> None:
    alembic_cfg = Config()
    alembic_cfg.set_main_option('script_location', script_location)
    alembic_cfg.set_main_option('sqlalchemy.url', dsn)
    command.upgrade(alembic_cfg, 'head')
    
@app.on_event('startup')
async def app_startup():
    asyncio.create_task(Consolidator().start())

 
if __name__ == "__main__":
    run_migrations("migrations", "sqlite:///energydb.sqlite")
    uvicorn.run(app, host="0.0.0.0", port=8000)