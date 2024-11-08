import json
import random
from datetime import datetime, timedelta
from googleapiclient.errors import HttpError
from google_calendar import CalendarManager


class Planner:
    def __init__(self, goals_file="data/goals.json"):
        self.goals_file = goals_file
        self.goals = self.load_goals()
        self.calendar_manager = CalendarManager()

    def load_goals(self):
        """Load goals from a JSON file and return a list of goal dictionaries."""
        try:
            with open(self.goals_file, "r") as file:
                goals = json.load(file)
                return goals
        except FileNotFoundError:
            print(f"Error: {self.goals_file} not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from {self.goals_file}.")
            return []

    def schedule_goals(self):
        """Schedule goals in Google Calendar randomly over the next week."""
        if not self.goals:
            print("No goals to schedule.")
            return

        now = datetime.utcnow()
        for goal in self.goals:
            # Randomize start date within the next 7 days
            start_date = now + timedelta(days=random.randint(1, 7))
            start_time = start_date.replace(hour=random.randint(9, 17), minute=0)
            end_time = start_time + timedelta(minutes=goal["duration"])

            try:
                self.calendar_manager.create_event(
                    title=goal["title"],
                    description=goal["description"],
                    start_time=start_time,
                    end_time=end_time,
                )
                print(f"Scheduled: {goal['title']} on {start_time}")
            except HttpError as error:
                print(f"An error occurred: {error}")
