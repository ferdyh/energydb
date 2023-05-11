from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from app.database import Database

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

db = Database()

app.mount("/web", StaticFiles(directory="./web/dist/"), name="web")

@app.get("/")
def root():
    return RedirectResponse(url=f"/web/index.html")

@app.get("/metrics/month")
def metrics_month(start: str = "2023-05-08"):
    return db.get_month_metrics()

@app.get("/metrics/day")
def metrics_month(start: str = "2023-05-08"):
    return db.get_day_metrics()
