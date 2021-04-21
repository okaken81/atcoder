import io
import sys

_INPUT = """\
1
273 691
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

a, b, c = [0]*n, [0]*n, [0]*n

for i in range(n):
    a[i], b[i] = map(int, input().split())
    c[i] = a[i]*2 + b[i]

a_all = sum(a)
c.sort(reverse=True)

for i in range(n):
    a_all -= c[i]
    if a_all < 0:
        print(i+1)
        exit()