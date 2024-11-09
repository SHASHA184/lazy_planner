from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base


class GoalModel(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    duration = Column(Integer)
    scheduled_time = Column(DateTime)
    completed = Column(Boolean, default=False)
