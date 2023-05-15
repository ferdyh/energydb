from fastapi import APIRouter
from database import get_session
from sqlalchemy import select

router = APIRouter(prefix="/readings")

@router.get("/")
def list():
    with get_session() as session:
        return session.query(Meter).all()