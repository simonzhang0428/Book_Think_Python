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
k2 = reverse_lookup(h, 10)
print(k2)
