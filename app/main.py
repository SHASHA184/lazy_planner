# app/main.py
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import goals


# Create all tables asynchronously (if needed)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Initialize FastAPI application
app = FastAPI(on_startup=[init_models])

# Include routers
app.include_router(goals.router)


# @app.post("/goals/", response_model=GoalResponse)
# async def add_goal(goal: Goal):
#     """Add a new goal and schedule it on Google Calendar."""
#     try:
#         result = planner.add_and_schedule_goal(goal.dict())
#         return GoalResponse(**result)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @app.get("/goals/", response_model=List[GoalResponse])
# async def list_goals():
#     """List all goals currently in the system."""
#     return planner.get_scheduled_goals()
