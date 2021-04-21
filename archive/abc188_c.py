import io
import sys

_INPUT = """\
4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4

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
a = list(map(int, input().split()))

half = int(2**n/2)

left = max(a[:half])
right = max(a[half:])

print(a.index(min(left, right)) +1)