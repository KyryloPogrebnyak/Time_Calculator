def add_time(start_time, duration, starting_day=None):
    # Parse the start_time
    start_time_parts = start_time.split()
    start_time = start_time_parts[0]
    period = start_time_parts[1]

    start_time_parts = start_time.split(":")
    start_hour = int(start_time_parts[0])
    start_minute = int(start_time_parts[1])

    # Parse the duration
    duration_parts = duration.split(":")
    duration_hour = int(duration_parts[0])
    duration_minute = int(duration_parts[1])

    # Calculate the total minutes
    total_minutes = start_hour * 60 + start_minute

    if period == "PM":
        total_minutes += 12 * 60  # Convert to 24-hour format if PM

    total_minutes += duration_hour * 60 + duration_minute

    # Calculate the new time
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60

    # Determine the period (AM or PM)
    if new_hour >= 12:
        new_period = "PM"
    else:
        new_period = "AM"

    # Convert new_hour to 12-hour format
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    # Calculate the number of days passed
    days_passed = total_minutes // (24 * 60)

    # Determine the day of the week if starting_day is provided
    if starting_day:
        starting_day = starting_day.lower().capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        starting_day_index = days_of_week.index(starting_day)
        new_day_index = (starting_day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        new_time = f"{new_hour}:{new_minute:02} {new_period}, {new_day}"
    else:
        new_time = f"{new_hour}:{new_minute:02} {new_period}"

    # Add " (next day)" or " (X days later)" if needed
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
