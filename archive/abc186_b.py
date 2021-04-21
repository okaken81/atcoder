import io
import sys

_INPUT = """\
3 2
4 4
4 4
4 4
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

h, w = map(int, input().split())

a = []

for _ in range(h):
    a.append(list(map(int, input().split())))

a = sum(a, [])
min = min(a)

print(sum(a) - min*len(a))