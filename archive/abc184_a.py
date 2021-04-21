import io
import sys

_INPUT = """\
100 100
100 100
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

a, b = map(int, input().split())
c, d = map(int, input().split())

print(a * d - b * c)
