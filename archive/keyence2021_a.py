import io
import sys

_INPUT = """\
20
715806713 926832846 890153850 433619693 890169631 501757984 778692206 816865414 50442173 522507343 546693304 851035714 299040991 474850872 133255173 905287070 763360978 327459319 193289538 140803416
974365976 488724815 821047998 371238977 256373343 218153590 546189624 322430037 131351929 768434809 253508808 935670831 251537597 834352123 337485668 272645651 61421502 439773410 621070911 578006919
"""
sys.stdin = io.StringIO(_INPUT)

# import numpy as np
# import pandas as pd
# import math
# import itertools
# import collections

# a = list(map(int, input().split()))
# n = int(input())
# d, t, s = map(int, input().split())

#### ----------------------------------

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_max = 0
c_max = 0

for i in range(n):
    if a[i] > a_max:
        a_max = a[i]
    if a_max * b[i] > c_max:
        c_max = a_max * b[i]
    print(c_max)