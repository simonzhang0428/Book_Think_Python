# infile = open('test.txt')
# with open('test.txt') as infile:
#     for line in infile:
#         line = line.rstrip()
#         words = line.split()
#         for word in words:
#             word = word.rstrip(".,?!")
#             print(word)
#

# using with, no need to close file
# infile.close()

# input_string = "United State: 3000"
# result = input_string.rsplit(":", 1)
# print(result)
import os


def has_no_e(word):
    for char in word:
        if char == 'e':
            return False
    return True


def avoids(word, forbidden):
    for char in word:
        if char in forbidden:
            return False
    return True


def uses_only(word, allowed):
    for char in word:
        if char not in allowed:
            return False
    return True


def uses_all(word, required):
    for char in required:
        if char not in word:
            return False
    return True
    # reduction to precious solved problem
    # return uses_only(required, word)


def is_abecedarian(word):
    previous = word[0]
    for char in word:
        if char < previous:
            return False
        previous = char
    return True


def is_abecedarian2(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian2(word[1:])


def is_abecedarian3(word):
    i = 0
    while i < len(word)-1:
        if word[i] > word[i+1]:
            return False
        i += 1
    return True


fin = open('words.txt')
cwd = os.getcwd()
abspath = os.path.abspath('File.py')
print(cwd)
print(abspath)
print(os.listdir(cwd))

# for line in fin:
#     word = line.strip()
#     if len(word) > 20:
#         print(word)


# count, total = 0, 0
# for line in fin:
#     word = line.strip()
#     total += 1
#     if has_no_e(word):
#         print(word)
#         count += 1
#
# print('without \'e\' percentage:', round(count / total, 3))

# count = 0
# forbidden = input('Enter forbidden letters: ')
# for line in fin:
#     word = line.strip()
#     if avoids(word, forbidden):
#         print(word)
#         count += 1
#
# print('without {} count is {}'.format(forbidden, count))

# count = 0
# allowed = input('Enter allowed letters: ')
# for line in fin:
#     word = line.strip()
#     if uses_only(word, allowed):
#         print(word)
#         count += 1
#
# print('only use {} count is {}'.format(allowed, count))


count = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        # print(word)
        count += 1

print('abecedarian word count is', count)

fin.close()
