import io
import sys

_INPUT = """\
123 234
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

a, b= map(int, input().split())

a = sum(list(map(int, str(a))))
b = sum(list(map(int, str(b))))

if a > b:
    print(a)
else:
    print(b)