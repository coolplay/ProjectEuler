"""Number letter counts"""

table = {
        1  : 'one',
        2  : 'two',
        3  : 'three',
        4  : 'four',
        5  : 'five',
        6  : 'six',
        7  : 'seven',
        8  : 'eight',
        9  : 'nine',
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
        20 : 'twenty',
        30 : 'thirty',
        40 : 'forty',
        50 : 'fifty',
        60 : 'sixty',
        70 : 'seventy',
        80 : 'eighty',
        90 : 'ninety',
        100: 'hundred',
        1000:'thousand',
        }

def _number2letter(i):
    """Generate sequence of letters corresponding to integer sequence `seq`

    seq should be numbers in range [1, 100)
    """
#   for i in seq:
    assert 0 < i < 100
    mod = i % 10
    if i < 20 or mod == 0:
        return table[i]
    else:
        return table[i-mod] + ' ' + table[mod]
#       return table[i-mod] + '-' + table[mod]


def number2letter(seq):
    """Generate sequence of letters corresponding to integer sequence `seq`

    seq should be numbers in range [1, 1000)
    """
    for i in seq:
        if 0 < i < 100:
            yield _number2letter(i)
        elif i < 1000:
            m = 100
            div, mod = divmod(i, m)
            if mod == 0:
                yield '{} {}'.format(table[div], table[m])
            else:
                yield '{} {} and {}'.format(table[div], table[m],
                        _number2letter(mod))
        elif i == 1000:
            yield 'one thousand'

print sum(len(i.replace(' ',''))  for i in number2letter(xrange(1, 1001)))
