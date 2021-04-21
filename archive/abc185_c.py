import io
import sys

_INPUT = """\
17
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

l = int(input())

ans = 1
ans2 = 1

for i in range(11):
    ans = ans * (l - 1 - i)
    ans2 = ans2 * (11 - i)

print(ans // ans2)