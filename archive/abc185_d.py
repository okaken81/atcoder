import io
import sys

_INPUT = """\
1 0
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

n, m = map(int, input().split())

if m == 0:
    print(1)
    exit()

if n == m:
    print(0)
    exit()

a = list(map(int, input().split()))
a.sort()

a0 = 0
b = [0] * m

for i in range(m):
    b[i] = a[i] - a0 - 1
    a0 = a[i]

b.append(n - a[-1])

b = [i for i in b if i != 0]

k = min(b)

ans = 0

for i in range(len(b)):
    if b[i] % k == 0:
        ans += b[i] // k
    else:
        ans += b[i] // k + 1

print(ans)