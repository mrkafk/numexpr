#!/usr/bin/env python

import numpy as np
import numexpr as ne

import random

#a=np.array(['abc', 'def', 'xyz', 'x11','za', ''])
# print ne.evaluate('"abc" == a')

# haystacks = np.array(['abckkk', 'adef', 'xyz',   'x11abcp','za', 'abc'])
# needles =   np.array(['abc',    'def',  'aterr', 'oot',    'zu', 'ab' ])
# print ne.evaluate('contains(haystacks, needles)')

# print ne.evaluate('contains(haystack, "abc")')
# print ne.evaluate('contains("abcd", haystack)')
# withemptystr = np.array(['abc', 'def', ''])
# print ne.evaluate('contains("abcd", withemptystr)')
# print ne.evaluate('contains(withemptystr, "")')


# needles =  np.array(['abc', 'def', 'aterr', 'oot', 'zu', 'ab c', ' abc', 'abc'])
# needles =  np.array([' abc', 'abc'])

# FAILS
# needles =  np.array(['abc', 'ab c', ' abc', 'abc'])
# res = ne.evaluate('contains("test abc here", needles)')
# print res


# needles =  np.array(['abc', 'ab c', ' xyz', 'abc'])
# res = ne.evaluate('contains("test abc here", needles)')
# print res

s = "It was the White Rabbit, trotting slowly back again, and looking anxiously about as it went, as if it had lost something; and she heard it muttering to itself 'The Duchess! The Duchess! Oh my dear paws! Oh my fur and whiskers! She'll get me executed, as sure as ferrets are ferrets! Where CAN I have dropped them, I wonder?' Alice guessed in a moment that it was looking for the fan and the pair of white kid gloves, and she very good-naturedly began hunting about for them, but they were nowhere to be seen--everything seemed to have changed since her swim in the pool, and the great hall, with the glass table and the little door, had vanished completely."


def splitrand(s, lo, hi):
    i = 0
    out = [0]
    while out[-1] < len(s):
        i += random.randint(lo, hi)
        out.append(i)
    s2 = []
    for i in range(1, len(out)):
        x1 = out[i - 1]
        x2 = out[i]
        s2.append(s[x1:x2])
    return s2

# print splitrand(s, 2, 7)

# print splitrand(s, 3, 6)

big = [
    'It wa', 's the', ' W', 'hit', 'e ', 'Ra', 'bb', 'it, t', 'ro', 'tting s', 'lowly', ' back ', 'agai', 'n, and', ' l', 'ookin', 'g ', 'an', 'xiously', ' about ', 'as it w', 'ent, as', ' if ', 'it had', ' los', 't ', 'so', 'mething', '; and', ' she h', 'eard ', 'it ', 'mutteri', 'ng to', ' itself', " 'The ", 'Duchess', '! ', 'Th', 'e ', 'Duchess', '! Oh m', 'y de', 'ar paws', '! ', 'Oh my ', 'fu', 'r and w', 'hiskers', "! She'", 'll ', 'get', ' me ', 'execute', 'd,', ' a', 's ', 'su', 're as ', 'fe', 'rrets', ' are f', 'errets!', ' Wher', 'e CAN', ' I ha', 've dro', 'pped t', 'hem', ', I ', 'won', "der?' A",
    'lice g', 'uess', 'ed ', 'in a m', 'omen', 't that', ' i', 't was l', 'ook', 'ing f', 'or th', 'e ', 'fan and', ' th', 'e p', 'air o', 'f whit', 'e ki', 'd glove', 's, and ', 'she v', 'ery ', 'good-na', 'tu', 'redl', 'y be', 'gan hun', 'ti', 'ng abou', 't for t', 'he', 'm, bu', 't t', 'hey ', 'were n', 'owhere', ' to b', 'e s', 'een-', '-eve', 'rythi', 'ng see', 'me', 'd ', 'to ha', 've', ' c', 'hanged', ' sinc', 'e her s', 'wim ', 'in the ', 'pool,', ' an', 'd the g', 'rea', 't h', 'all, wi', 'th the ', 'glas', 's t', 'able an', 'd th', 'e littl', 'e door,', ' had va', 'ni', 'shed co', 'mpletel', 'y.']
small = [
    'It w', 'as th', 'e Whit', 'e Rab', 'bit,', ' tro', 'tting', ' sl', 'owly', ' back ', 'again,', ' and', ' lo', 'okin', 'g a', 'nxious', 'ly a', 'bou', 't a', 's it w', 'ent,', ' as i', 'f it', ' had l', 'ost', ' some', 'thi', 'ng; a', 'nd ', 'she ', 'heard ', 'it mut', 'terin', 'g to ', 'its', 'elf ', "'The", ' Duch', 'ess! T', 'he ', 'Duches', 's! Oh ', 'my dea', 'r paws', '! Oh ', 'my f', 'ur ', 'and ', 'whiske', 'rs! ', 'She', "'ll g", 'et me', ' ex', 'ecu', 'ted, ', 'as su', 're a', 's f', 'errets', ' are f', 'errets', '! Wh', 'ere ', 'CAN', ' I hav', 'e d', 'roppe', 'd t', 'hem,', ' I wo', 'nder?', "' A", 'lice',
    ' gu', 'essed', ' in a', ' mom', 'ent ', 'tha', 't it w', 'as ', 'looki', 'ng f', 'or ', 'the fa', 'n and ', 'the', ' pai', 'r of w', 'hit', 'e kid', ' glo', 'ves', ', and ', 'she ', 'very g', 'ood', '-na', 'turedl', 'y be', 'gan h', 'unt', 'ing', ' about', ' for t', 'hem', ', but', ' they ', 'wer', 'e nowh', 'ere to', ' be', ' se', 'en--', 'ever', 'ythin', 'g seem', 'ed ', 'to ', 'have c', 'hang', 'ed ', 'since', ' he', 'r swim', ' in', ' the', ' pool,', ' and', ' the g', 'reat ', 'hal', 'l, w', 'ith', ' th', 'e gl', 'ass t', 'abl', 'e and ', 'the', ' li', 'ttle', ' doo', 'r, ha', 'd v', 'ani', 'shed c', 'omp', 'lete', 'ly.']


def test5():
    from itertools import product
    small = ['It w', 'as th', 'e Whit', 'e Rab', 'bit,', ' tro', 'tting', ' sl', 'owly', ' back ', 'again,', ' and', ' lo', 'okin', 'g a', 'nxious', 'ly a', 'bou', 't a', 's it w', 'ent,', ' as i', 'f it', ' had l', 'ost', ' some', 'thi', 'ng; a', 'nd ', 'she ', 'heard ', 'it mut', 'terin', 'g to ', 'its', 'elf ', "'The", ' Duch', 'ess! T', 'he ', 'Duches', 's! Oh ', 'my dea', 'r paws', '! Oh ', 'my f', 'ur ', 'and ', 'whiske', 'rs! ', 'She', "'ll g", 'et me', ' ex', 'ecu', 'ted, ', 'as su', 're a', 's f', 'errets', ' are f', 'errets', '! Wh', 'ere ', 'CAN', ' I hav', 'e d', 'roppe', 'd t', 'hem,', ' I wo', 'nder?', "' A", 'lice',
        ' gu', 'essed', ' in a', ' mom', 'ent ', 'tha', 't it w', 'as ', 'looki', 'ng f', 'or ', 'the fa', 'n and ', 'the', ' pai', 'r of w', 'hit', 'e kid', ' glo', 'ves', ', and ', 'she ', 'very g', 'ood', '-na', 'turedl', 'y be', 'gan h', 'unt', 'ing', ' about', ' for t', 'hem', ', but', ' they ', 'wer', 'e nowh', 'ere to', ' be', ' se', 'en--', 'ever', 'ythin', 'g seem', 'ed ', 'to ', 'have c', 'hang', 'ed ', 'since', ' he', 'r swim', ' in', ' the', ' pool,', ' and', ' the g', 'reat ', 'hal', 'l, w', 'ith', ' th', 'e gl', 'ass t', 'abl', 'e and ', 'the', ' li', 'ttle', ' doo', 'r, ha', 'd v', 'ani', 'shed c', 'omp', 'lete', 'ly.']
    big = ['It wa', 's the', ' W', 'hit', 'e ', 'Ra', 'bb', 'it, t', 'ro', 'tting s', 'lowly', ' back ', 'agai', 'n, and', ' l', 'ookin', 'g ', 'an', 'xiously', ' about ', 'as it w', 'ent, as', ' if ', 'it had', ' los', 't ', 'so', 'mething', '; and', ' she h', 'eard ', 'it ', 'mutteri', 'ng to', ' itself', " 'The ", 'Duchess', '! ', 'Th', 'e ', 'Duchess', '! Oh m', 'y de', 'ar paws', '! ', 'Oh my ', 'fu', 'r and w', 'hiskers', "! She'", 'll ', 'get', ' me ', 'execute', 'd,', ' a', 's ', 'su', 're as ', 'fe', 'rrets', ' are f', 'errets!', ' Wher', 'e CAN', ' I ha', 've dro', 'pped t', 'hem', ', I ', 'won', "der?' A",
        'lice g', 'uess', 'ed ', 'in a m', 'omen', 't that', ' i', 't was l', 'ook', 'ing f', 'or th', 'e ', 'fan and', ' th', 'e p', 'air o', 'f whit', 'e ki', 'd glove', 's, and ', 'she v', 'ery ', 'good-na', 'tu', 'redl', 'y be', 'gan hun', 'ti', 'ng abou', 't for t', 'he', 'm, bu', 't t', 'hey ', 'were n', 'owhere', ' to b', 'e s', 'een-', '-eve', 'rythi', 'ng see', 'me', 'd ', 'to ha', 've', ' c', 'hanged', ' sinc', 'e her s', 'wim ', 'in the ', 'pool,', ' an', 'd the g', 'rea', 't h', 'all, wi', 'th the ', 'glas', 's t', 'able an', 'd th', 'e littl', 'e door,', ' had va', 'ni', 'shed co', 'mpletel', 'y.']
    p = list(product(small, big))
    python_in = [x[0] in x[1] for x in p]
    a = [x[0] for x in p]
    b = [x[1] for x in p]
    res = [bool(x) for x in ne.evaluate('contains(b, a)')]
    print res == python_in


test5()
