# coding: utf-8
# string practice
# 05/05/2020



fruit = 'banana'
letter = fruit[0]
l = len(fruit)
last = fruit[-1]
print(fruit[:3])
print(fruit[:])
print(fruit[3:])

# string is immutable, dose not support item assignment
# fruit[0] = 'a'

# Create new string using slice
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

# traversal
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

for letter in fruit:
    print(letter)

# given a string, print backward
def traversal_backward(input_string):
    index = len(input_string) - 1
    while index >= 0:
        letter = input_string[index]
        print(letter)
        index = index - 1

traversal_backward('123')
traversal_backward('hello')



# The following example shows how to use concatenation (string addition)
# and a for loop to generate an abecedarian series
# (that is, in alphabetical order).
# the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.
# This loop outputs these names in order:

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    print(letter + suffix)

# find the letter in word, return index
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('hello', 'h'))
print(find('hello', 'H'))

# given the index in word where it should start looking
def find(word, letter, start_pos):
    index = start_pos
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find('hello', 'h', 1))
print(find('hello', 'o', 3))

# Count the letter appear times in the given word
def count(word, letter):
    counter = 0
    for char in word:
        if char == letter:
            counter = counter + 1
    return counter

print(count('hello', 'l'))
print(count('hello', 'H'))


# A method call is called an invocation
word = 'banana'
print(word.upper()) # not change the original word
print(word)
print(word.find('a'))
print(word.find('na'))
print(word.find('na', 3)) # 3 is the start index

name = 'bob'
print(name.find('b', 1, 2)) # 1 is start, 2 is end

# in operator
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('apples', 'oranges')

# check whether given two words are reverse
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while i < len(word1):
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True

print(is_reverse('hello', 'olleh'))
print(is_reverse('ef', 'fe'))

# string default count method
print(name, name.count('b'))

# A step size of -1 goes through the word backwards,
# so the slice [::-1] generates a reversed string
# A palindrome is a word that is spelled the same backward
# and forward, like “noon” and “redivider”.
# Recursively, a word is a palindrome if the first and last letters are the same
# and the middle is a palindrome.

def first(word): return word[0]
def last(word): return word[-1]
def middle(word): return word[1:-1]

def is_palinfrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palinfrome(middle(word))

def is_palinfrome2(word):
    return word == word[::-1]

print(is_palinfrome2('allen'))
print(is_palinfrome2('bob'))


# A Caesar cypher is a weak form of encryption that involves “rotating” each letter
# by a fixed number of places.
# To rotate a letter means to shift it through the alphabet, 
# wrapping around to the beginning if necessary,
# so ‘A’ rotated by 3 is ‘D’ and ‘Z’ rotated by 1 is ‘A’.


def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))
