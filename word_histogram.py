import random
import string

for i in range(10):
    x = random.random()
    print(x)

for i in range(10):
    x = random.randint(5, 10)
    print(x)

t = [1, 2, 3]
for i in range(10):
    x = random.choice(t)
    print(x)


def histogram1(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram1('jdfljsdlkfjskdjfjsdlfjdks')
print(h)
print(h.get('d'))
print(h.get('a'))
print(h.get('a', 1))


def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)  # given key, return value, not found default 0
    return d


h = histogram('jdfljsdlkfjskdjfjsdlfjdks')
print(h)


def print_hist(h):
    for key in h:
        print(key, h[key])


print_hist(h)


def print_order_hist(h):
    for key in sorted(h):
        print(key, h[key])


def print_dash():
    print('-' * 20)


print_dash()
print_order_hist(h)


def reverse_lookup(d, v):
    for key in d:
        if d[key] == v:
            return key
    raise LookupError("Not found!")


print_dash()
k = reverse_lookup(h, 6)
print(k)
print_dash()


# k2 = reverse_lookup(h, 10)
# print(k2)


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


hist = histogram('parrot')
print_hist(hist)
inverse = invert_dict(hist)
print(inverse)
print_hist(inverse)


def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


def total_words(hist):
    return sum(hist.values())


def different_words(hist):
    return len(hist)


print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
hist = process_file('emma.txt')
# print_hist(hist)
print('Total number of words: ', total_words(hist))
print('Number of different words: ', different_words(hist))


def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):  # default optional parameter is  10
    t = most_common(hist)
    print('The most common words are: ')
    for freq, word in t[:num]:
        print(word, freq, sep='\t')


print_most_common(hist, 20)  # override the optional parameter


def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


def subtract2(d1, d2):
    return set(d1) - set(d2)

words = process_file('words.txt')
diff = subtract(hist, words)

print('Words in book that are not in the word list:')
for word in diff:
    print(word, end=' ')
print()


diff2 = subtract2(hist, words)
print('Words in book that are not in the word list:')
for word in diff2:
    print(word, end=' ')
