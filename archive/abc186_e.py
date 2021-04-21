import io
import sys

_INPUT = """\
4
10 4 3
1000 11 2
998244353 897581057 595591169
10000 6 14
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

import math

t = int(input())

for _ in range(t):
    n, s, k = map(int, input().split())
    if s % math.gcd(n, k) != 0:
        print(-1)

# n*x = k*y + s