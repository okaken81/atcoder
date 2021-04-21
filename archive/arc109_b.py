import io
import sys

_INPUT = """\
999999998765257139
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

l = 0
r = n + 1

while abs(r-l) > 1:
    m = (r + l) // 2
    if m * (m + 1) // 2 <= n + 1:
        l = m
    else:
        r = m

print(n - l + 1)