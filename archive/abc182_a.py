import io
import sys

_INPUT = """\
10000 0
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

print((2 * a + 100) - b)
