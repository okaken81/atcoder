import io
import sys

_INPUT = """\
1
1 1000000
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

sum = 0

for i in range(n):
    a, b = map(int, input().split())
    sum += (a + b) * (b - a + 1) // 2

print(sum)
