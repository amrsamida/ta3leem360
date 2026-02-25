from sqlalchemy import Column, Integer, String
from app.database import Base


class Center(Base):
    __tablename__ = "centers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    description = Column(String, nullable=True)