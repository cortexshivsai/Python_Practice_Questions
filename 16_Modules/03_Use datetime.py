# Use Datetime
# Import the datetime class from the datetime module
from datetime import datetime

# Get the current date and time
current = datetime.now()

# Display the complete date and time
print("Current date and time:", current)

# Display only the date
print("Current date:", current.date())

# Display only the time
print("Current time:", current.time())

# Display date and time in a custom format
formatted_date = current.strftime("%d-%m-%Y")
formatted_time = current.strftime("%H:%M:%S")

print("Formatted date:", formatted_date)
print("Formatted time:", formatted_time)


"""
Example output:
Current date and time: 2026-10-12 16:50:00.000000
Current date: 2026-10-12
Current time: 16:50:00
Formatted date: 12-10-2026
Formatted time: 16:50:00

Code       Meaning

%d          Day

%m          Month

%Y          Four Digit Year

%H          Hour in 24-hour format

%M          Minutes

%S          Seconds


strftime() converts a date or time into a formatted string.
"""