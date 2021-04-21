import io
import sys

_INPUT = """\
20 10
xxxxxxxxxxxxxxxxxxxx
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

n, x = map(int, input().split())
s = list(input())

for i in range(n):
    if s[i] == 'o':
        x += 1
    elif x > 0:
        x -= 1

print(x)