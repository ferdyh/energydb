from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from app.database import Database

app = FastAPI()
db = Database()

app.mount("/web", StaticFiles(directory="./web"), name="web")

@app.get("/")
def root():
    return RedirectResponse(url=f"/web/index.html")

@app.get("/metrics/month")
def metrics_month(start: str = "2023-05-08"):
    return db.get_month_metrics()

@app.get("/metrics/day")
def metrics_month(start: str = "2023-05-08"):
    return db.get_day_metrics()
