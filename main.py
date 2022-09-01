# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


# Test Example:
#start = "11:43 PM"; duration = "24:20"; startingWeekDay = "tUeSdAy"
#result = add_time(start, duration, startingWeekDay)
#print(start, duration, startingWeekDay)
#print(result)


# Run unit tests automatically
main(module='test_module', exit=False)