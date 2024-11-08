from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    completed: bool = False
