# app/routers/goals.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_db
from app.google_calendar import CalendarManager
from datetime import datetime, timedelta
from typing import List

router = APIRouter()
calendar_manager = CalendarManager()


@router.post("/goals/", response_model=schemas.GoalResponse)
async def create_goal(goal: schemas.GoalCreate, db: AsyncSession = Depends(get_db)):
    scheduled_time = datetime.utcnow() + timedelta(days=1)  # Example scheduling logic
    end_time = scheduled_time + timedelta(minutes=goal.duration)

    await calendar_manager.create_event(
        title=goal.title,
        description=goal.description,
        start_time=scheduled_time,
        end_time=end_time,
    )

    db_goal = await crud.create_goal(db=db, goal=goal, scheduled_time=scheduled_time)
    return schemas.GoalResponse(
        id=db_goal.id, title=db_goal.title, scheduled_time=db_goal.scheduled_time
    )


@router.get("/goals/", response_model=List[schemas.GoalResponse])
async def read_goals(db: AsyncSession = Depends(get_db)):
    return await crud.get_goals(db=db)


@router.get("/goals/{goal_id}", response_model=schemas.GoalResponse)
async def read_goal(goal_id: int, db: AsyncSession = Depends(get_db)):
    db_goal = await crud.get_goal(db=db, goal_id=goal_id)
    if db_goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return db_goal
