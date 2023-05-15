from fastapi import APIRouter
from database import get_session

import uuid

from models import Meter
from routers import readings

router = APIRouter(prefix="/meters")

@router.get("/")
def list():
    with get_session() as session:
        return session.query(Meter).all()
    
@router.get("/{meter_id}")
def get(meter_id):
    with get_session() as session:
        return session.get(Meter, meter_id)
    
@router.post("/")
def create(meter: Meter):
    with get_session() as session:
        meter.id = uuid.uuid4()
        session.add(meter)
        return meter

    
router.include_router(readings.router, prefix="/{meter_id}")