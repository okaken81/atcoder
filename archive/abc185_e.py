import io
import sys

_INPUT = """\
4 3
1 2 1 3
1 3 1
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

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(n, m)
print(a)
print(b)