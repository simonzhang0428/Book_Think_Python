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
