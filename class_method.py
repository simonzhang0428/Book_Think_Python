class Time:
    """Represents the time of day.

    attributes: hours, minutes, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):  # type-based dispatch, depending parameter type
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):  # right-side add
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
        # return self.hour * 3600 + self.minute * 60 + self.second

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


start = Time()
start.hour = 9
start.minute = 45
start.second = 00
start.print_time()  # object is the active agent "oop"
Time.print_time(start)  # function is the active agent

end = start.increment(1337)
end.print_time()
print('True:', end.is_after(start))

t1 = Time()
t2 = Time(9)
t3 = Time(9, 45)
t1.print_time()
t2.print_time()
t3.print_time()
print(t3)  # __str__ method

start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)  # add time object
print(start + 1337)  # add second
print(1337 + start)  # not commutative, order matters! radd!

total = sum([t1, t2, t3])  # polymorphism, work with different type
print(total)
print('True:', hasattr(t1, 'hour'))  # check attribute
print(vars(t2))  # return dictionary map from attribute to their value


def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))


print_attributes(t2)
