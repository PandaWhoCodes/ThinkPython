"""
Write a function called print_time that takes a
Time object and prints it in the
form hour:minute:second. Hint: the format sequence
'%.2d' prints an integer using at least
two digits, including a leading zero if necessary.
"""


class Time(object):
    """
    This is our time object
    """


myTime = Time()
myTime.hour = 14
myTime.minutes = 1
myTime.seconds = 45
print(str(myTime.hour) + ":" + str(myTime.minutes) + ":" + str(myTime.seconds))
