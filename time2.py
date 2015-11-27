"""
Write a boolean function called is_after that
takes two Time objects, t1 and t2,
and returns True if t1 follows t2 chronologically
and False otherwise. Challenge: don't use an if
statement.
"""


class time(object):
    """
    Object for time
    """


def to_seconds(t):
    return t.seconds + t.minutes * 60 + t.hour * 360


def is_after(t1, t2):
    tt1 = to_seconds(t1)
    tt2 = to_seconds(t2)
    return tt1 > tt2


if __name__ == '__main__':
    time1 = time()
    time2 = time()
    time1.hour = 14
    time1.minutes = 1
    time1.seconds = 45
    time2.hour = 14
    time2.minutes = 2
    time2.seconds = 46
    print(is_after(time1, time2))
