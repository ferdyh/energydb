from pydantic import BaseModel
import datetime

class Meter(BaseModel):
    meter: str
    source: str
    metrics: list

class Metric(BaseModel):
    date: datetime.date
    usage: float