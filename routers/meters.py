from fastapi import APIRouter
from database import get_session

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
        session.add(meter)
        session.commit()
        session.refresh(meter)
        return meter
    
@router.delete("/{meter_id}")
def delete(meter_id):
    with get_session() as session:
        meter = session.get(Meter, meter_id)
        session.delete(meter)
        session.commit()

router.include_router(readings.router, prefix="/{meter_id}")