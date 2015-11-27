"""
Write a correct version of increment that doesn't contain any loops.
Anything that can be done with modifiers can also be done with pure functions. In fact,
some programming languages only allow pure functions. There is some evidence that
programs that use pure functions are faster to develop and less error-prone than programs
that use modifiers. But modifiers are convenient at times, and functional programs tend to
be less efficient.
In general, I recommend that you write pure functions whenever it is reasonable and resort
to modifiers only if there is a compelling advantage. This approach might be called a
functional programming style.
"""


class Time(object):
    """
    This is our time object
    """


def increment(seconds):
    if seconds > 60 and t.seconds < 60:
        temp = 60 - t.seconds
        seconds = seconds - temp
        t.seconds = 0
        t.minutes = t.minutes + 1

    if t.minutes > 60:
        t.hour = t.hour + 1
        t.minutes = 0

    if t.hour > 24:
        t.hour = 0

    if seconds < 60:
        t.seconds = t.seconds + seconds
        if t.seconds > 60:
            t.seconds = t.seconds - 60
            t.minutes = t.minutes + 1
            seconds = 0

    if seconds != 0:
        increment(seconds)


t = Time()
t.hour = 12
t.minutes = 11
t.seconds = 45

increment(195)
print(str(t.hour) + ":" + str(t.minutes) + ":" + str(t.seconds))
