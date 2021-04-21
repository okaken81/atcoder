import io
import sys

_INPUT = """\
3 5
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

x, y = map(int, input().split())

if x > y:
    x, y = y, x

if y - x < 3:
    print('Yes')
else:
    print('No')