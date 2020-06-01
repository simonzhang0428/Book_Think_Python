import copy
from datetime import datetime


class Time:
    """Represents the time of day.

    attributes: hours, minutes, second
    """


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 9
time2.minute = 00
time2.second = 00


def print_time(t: Time):
    print('%.2d : %.2d : %.2d' % (t.hour, t.minute, t.second))


print_time(time)


def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


# pure function, not modify parameter, has no effect(display, get input...)
def add_time(t1: Time, t2: Time):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum


# modifier, change the parameter.
def increment1(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)  # returns the quotient and remainder as a tuple
    time.hour, time.minute = divmod(minutes, 60)
    return time


print_time(int_to_time(time_to_int(time)))


def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def increment(time, seconds):
    seconds += time_to_int(time)
    return int_to_time(seconds)


print_time(increment(time, 11))
print_time(time)
print_time(add_time(time, time2))


def is_after(t1, t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


print('True:', is_after(time, time2))

time3 = Time()
time3.hour = 9
time3.minute = 00
time3.second = 00

add_time(time, time3)

b1 = datetime(1987, 4, 28)
print(b1)
