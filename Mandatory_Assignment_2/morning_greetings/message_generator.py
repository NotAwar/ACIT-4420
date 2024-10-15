import datetime

def generate_message(name: str) -> str:
    """
    Generates a personalized 'Good Morning' message, customized based on the day of the week.
    """
    weekday_messages = {
        0: "Start your week with energy!",  # Monday
        1: "Keep going, you're doing great!",  # Tuesday
        2: "Halfway there!",  # Wednesday
        3: "Almost at the finish line!",  # Thursday
        4: "It's Friday! Time to relax.",  # Friday
        5: "Enjoy your weekend!",  # Saturday
        6: "Recharge and prepare for the week ahead!",  # Sunday
    }

    day_of_week = datetime.datetime.now().weekday()  # Get current day (0=Monday, 6=Sunday)
    extra_message = weekday_messages.get(day_of_week, "Have a great day!")  # Default message

    return f"Good Morning, {name}! {extra_message}"
