#!/usr/bin/env python

import numpy as np
import numexpr as ne
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
needles =  np.array(['abc', 'ab c', ' abc', 'abc'])
res = ne.evaluate('contains("test abc here", needles)')
print res
