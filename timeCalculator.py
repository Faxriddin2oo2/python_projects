# Bismillah
"""
Created on Fri Oct 11 21:18:03 2024

@author: Faxriddin
"""

def add_time(start, duration, day_of_week=None):
    # Days of the week list
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split start time into components
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Adjust hour to 24-hour format based on AM/PM
    if period == "PM":
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Split duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add minutes and handle overflow
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    new_minute = total_minutes % 60

    # Add hours and handle day overflow
    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    new_hour = total_hours % 24

    # Convert back to 12-hour format
    if new_hour == 0:
        period = "AM"
        display_hour = 12
    elif new_hour < 12:
        period = "AM"
        display_hour = new_hour
    elif new_hour == 12:
        period = "PM"
        display_hour = 12
    else:
        period = "PM"
        display_hour = new_hour - 12

   
    if day_of_week:
        day_of_week = day_of_week.capitalize()
        day_index = days_of_week.index(day_of_week)
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
    

    new_time = f"{display_hour}:{new_minute:02d} {period}"


    if day_of_week:
        new_time += f", {new_day}"


    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tuesday"))
