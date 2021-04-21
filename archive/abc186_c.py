import io
import sys

_INPUT = """\
100000
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

ans = n

for i in range(n):
    if '7' in str(i+1):
        ans -= 1
    elif '7' in oct(i+1):
        ans -= 1

print(ans)
