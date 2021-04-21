import io
import sys

_INPUT = """\
1 100 1 100
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

a, b, x, y = map(int, input().split())

if a == b:
    ans = x
elif a > b:
    ans1 = (a - b - 1) * y + x
    ans2 = (a - b) * x + (a - b - 1) * x
    ans = min(ans1, ans2)
else:
    ans1 = (b - a) * y + x
    ans2 = (b - a) * x + (b - a + 1) * x
    ans = min(ans1, ans2)

print(ans)