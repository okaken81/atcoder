import io
import sys

_INPUT = """\
2 2 3
1 1 X
2 1 R
2 2 R
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

h, w, k = map(int, input().split())

print(h, w, k)