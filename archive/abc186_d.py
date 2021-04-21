import io
import sys

_INPUT = """\
3
5 1 2
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
a.sort()

ans = 0

for i in range(n):
    ans += -a[i] * (n-i-1) + a[i] * i

print(ans)