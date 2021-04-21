import io
import sys

_INPUT = """\
1 1
1 1
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

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

if r1 == r2 and c1 == c2:
    print(0)
    exit()

d1 = abs((r1 + c1) - (r2 + c2))
d2 = abs((r1 - c1) - (r2 - c2))
d = min(d1, d2)

if d == 0:
    print(1)
elif abs(r1 - r2) + abs(c1 - c2) <= 3:
    print(1)
elif d <= 3:
    print(2)
elif (abs(r1 - r2) - abs(c1 - c2)) % 2 == 0:
    print(2)
else:
    print(3)