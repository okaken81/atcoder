import io
import sys

_INPUT = """\
1000000000 987654321 123456789
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

a, b, c = map(int, input().split())

mod = 998244353

ans = a*(a + 1) * b*(b + 1) * c*(c + 1) // 8

print(ans % mod)