from sqlalchemy import Column, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Meter(Base):
    __tablename__ = "meters"

    id = Column("id", VARCHAR, primary_key=True)
    name = Column("name", VARCHAR)
    source = Column("source", VARCHAR)
    color = Column("color", VARCHAR)

    def __repr__(self) -> str:
        return f"Meter(id={self.id}, name={self.name}, source={self.source}, color={self.color})"
