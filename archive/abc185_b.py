import io
import sys

_INPUT = """\
20 1 30
1 10
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

n, m ,t = map(int, input().split())

n0 = n
a0 = 0
b0 = 0

for i in range(m):
    a1, b1 = map(int, input().split())
    if n - a1 + b0 <= 0:
        print('No')
        exit()
    else:
        n = n - a1 + b0 + b1 - a1
        a0 = a1
        b0 = b1
        if n > n0:
            n = n0

if n - t + b1 <= 0:
    print('No')
else:
    print('Yes')

