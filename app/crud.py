from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas
from sqlalchemy import select


async def create_goal(db: AsyncSession, goal: schemas.GoalCreate, scheduled_time):
    db_goal = models.GoalModel(
        title=goal.title,
        description=goal.description,
        duration=goal.duration,
        scheduled_time=scheduled_time,
        completed=False,
    )
    db.add(db_goal)
    await db.commit()
    await db.refresh(db_goal)
    return db_goal


async def get_goal(db: AsyncSession, goal_id: int):
    query = select(models.GoalModel).filter(models.GoalModel.id == goal_id)
    result = await db.execute(query)
    return result.scalars().first()


async def get_goals(db: AsyncSession):
    query = select(models.GoalModel)
    result = await db.execute(query)
    return result.scalars().all()
