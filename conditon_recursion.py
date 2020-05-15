# Write a script that reads the current time and
# converts it to a time of day in hours, minutes, and seconds,
# plus the number of days since the epoch.

import time

last_epoch = time.time()


def current_time(since_epoch):
    """Calculates current hour, minute, and second since given epoch;
    since epoch - in seconds.
    """
    hours_since = since_epoch // 60 // 60
    current_hour = hours_since - (hours_since // 24) * 24
    minutes_since = since_epoch // 60
    current_minute = minutes_since - (minutes_since // 60) * 60
    second_since = since_epoch // 1  # to round down seconds
    current_second = second_since - (second_since // 60) * 60
    return current_hour, current_minute, current_second


def days_since_epoch(epoch):
    """Returns number of days since given epoch;
    epoch - in seconds.
    """
    days = epoch // 60 // 60 // 24
    return days


print(current_time(last_epoch))
print(days_since_epoch(last_epoch))

"""
Exercise 5.2.
Fermat’s Last Theorem says that there are no positive integers a, b, and c such
that:
a**n + b**n = c**n
for any values of n greater than 2.
1.  Write  a  function  named check_fermat that  takes  four  parameters —
    a, b, c and n — and checks to see if Fermat’s theorem holds. If n is greater
    than 2 and
        a**n + b**n = c**n
    the program should print, “Holy smokes, Fermat was wrong!”. Otherwise the
    program should print, “No, that doesn’t work.”
2.  Write a function that prompts the user to input values for a, b, c and n,
    converts them to integers, and uses check_fermat to check whether they
    violate Fermat’s theorem.
"""


def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def prompting():
    a = input("Type your value of a: ")
    b = input("Type your value of b: ")
    c = input("Type your value of c: ")
    n = input("Type your value of n: ")

    check_fermat(int(a), int(b), int(c), int(n))


prompting()

"""
If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, you can.
(If the sum of two lengths equals the third, they form what is called a “degenerate” triangle.)
"""


def is_triangle(a, b, c):
    """print Yes if a, b, c can form a triangle;
    print No otherwise.

    a, b, c are integers.
    """
    if (a + b) < c or (a + c) < b or (b + c) < a:
        print('No')
    else:
        print('Yes')


is_triangle(3, 4, 5)
is_triangle(1, 1, 10)

side1 = int(input('Enter side 1:'))
side2 = int(input('Enter side 2:'))
side3 = int(input('Enter side 3:'))
is_triangle(side1, side2, side3)


def recurse(n, s):
    """

    :param n: positive integer, the times to recursive
    :param s: integer, start point
    :return: after n-th recursion, the final s
    """
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(3, 0)
