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
        d[c] += d.get(c, 1)
    return d


h = histogram('jdfljsdlkfjskdjfjsdlfjdks')
