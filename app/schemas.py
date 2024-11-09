from pydantic import BaseModel
from datetime import datetime


class GoalCreate(BaseModel):
    title: str
    description: str
    duration: int


class GoalResponse(BaseModel):
    id: int
    title: str
    scheduled_time: datetime
