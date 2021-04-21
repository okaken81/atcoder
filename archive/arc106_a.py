import io
import sys

_INPUT = """\
106
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

max_a = 38
max_b = 26

ans = -1

for a in range(1, max_a+1):
    if 3**a >= n:
        break
    for b in range(1, max_b+1):
        if 3**a + 5**b == n:
            print(a, b)
            ans = 1
            break
        elif 3**a + 5**b >= n:
            break
    if ans == 1:
        break

if ans == -1:
    print(ans)