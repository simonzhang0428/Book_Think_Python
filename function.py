# Write a function named right_justify that
# takes a string named s as a parameter and
# prints the string with enough leading spaces
# so that the last letter of the string is in column 70 of the display:


def right_justify(s):
    blank_space = 70 - len(s)
    return blank_space * ' ' + s


print(right_justify('monty'))


# function call inside function, parameter is also function
def print_spam():
    print('spam')


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_twice(f, n):
    f(n)
    f(n)


def do_four(f, n):
    do_twice(f, n)
    do_twice(f, n)


do_twice(print, 'spam')
do_four(print, 'spam')


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print('+ - - - -', end=' ')


def print_post():
    print('|        ', end=' ')


def print_beams():
    do_twice(print_beam)
    print('+')


def print_posts():
    do_twice(print_post)
    print('|')


def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)
    print_beams()


print_grid()


# grid 4*4
def one_four_one(f, g, h):
    f()
    do_four(g)
    h()


def print_plus():
    print('+', end=' ')


def print_dash():
    print('-', end=' ')


def print_bar():
    print('|', end=' ')


def print_space():
    print(' ', end=' ')


def print_end():
    print()


def nothing():
    "do nothing"


def print1beam():
    one_four_one(nothing, print_dash, print_plus)


def print1post():
    one_four_one(nothing, print_space, print_bar)


def print4beams():
    one_four_one(print_plus, print1beam, print_end)


def print4posts():
    one_four_one(print_bar, print1post, print_end)


def print_row():
    one_four_one(nothing, print4posts, print4beams)


def print_grid():
    one_four_one(print4beams, print_row, nothing)


print_grid()
