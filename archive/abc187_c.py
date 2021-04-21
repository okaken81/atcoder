import io
import sys

_INPUT = """\
6
a
!a
b
!c
d
!d
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
s = set(input() for _ in range(n))

for i in s:
    if '!' + i in s:
        print(i)
        exit()
print('satisfiable')