from typing import Optional
from sqlmodel import Field, SQLModel

import uuid

class Meter(SQLModel, table=True):
    __tablename__ = "meters"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    source: str
    color: str

    def __repr__(self) -> str:
        return f"Meter(id={self.id}, name={self.name}, source={self.source}, color={self.color})"
