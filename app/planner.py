import uuid
from datetime import datetime, timedelta
from googleapiclient.errors import HttpError
from app.google_calendar import CalendarManager
from typing import List, Dict


class Planner:
    def __init__(self):
        self.calendar_manager = CalendarManager()
        self.goals = []

    def add_and_schedule_goal(self, goal_data: Dict):
        """Add a new goal, assign it an ID, and schedule it on Google Calendar."""

        # Generate a unique ID for the goal
        goal_id = str(uuid.uuid4())

        # Define start time and calculate scheduled time
        start_time = datetime.utcnow() + timedelta(days=1)
        end_time = start_time + timedelta(minutes=goal_data["duration"])

        # Schedule the goal on Google Calendar
        try:
            self.calendar_manager.create_event(
                title=goal_data["title"],
                description=goal_data.get("description", ""),
                start_time=start_time,
                end_time=end_time,
            )
        except HttpError as error:
            print(f"An error occurred: {error}")
            raise

        # Create a complete goal object including ID and scheduled_time
        goal_with_id = {
            "id": goal_id,
            "title": goal_data["title"],
            "description": goal_data.get("description", ""),
            "duration": goal_data["duration"],
            "scheduled_time": start_time,
        }

        # Add the goal to the internal list
        self.goals.append(goal_with_id)

        return goal_with_id

    def get_scheduled_goals(self) -> List[Dict]:
        """Return the list of scheduled goals."""
        return self.goals
