# planner/utils.py

import random
import datetime


def get_random_time():
    # Generate a random time between 9 AM and 6 PM
    hour = random.randint(9, 17)
    minute = random.choice([0, 30])  # 0 or 30 minutes past the hour
    return datetime.time(hour, minute)
