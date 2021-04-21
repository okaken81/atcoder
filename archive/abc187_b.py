import io
import sys

_INPUT = """\
10
-31 -35
8 -36
22 64
5 73
-14 8
18 -58
-41 -85
1 -88
-21 -85
-11 82
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

x, y = [0]*n, [0]*n

for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0

for i in range(n-1):
    for j in range(i+1, n):
        t = (y[i] - y[j]) / (x[i] - x[j])
        if t >= -1 and t <= 1:
            ans += 1

print(ans)