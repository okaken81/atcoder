import io
import sys

_INPUT = """\
5
1000 1000 1000 1000 1000
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

ans = 0
ans_num = 0

for k in range(2, 1000):
    tmp = 0
    for i in range(n):
        if a[i] % k == 0:
            tmp += 1
    if ans_num < tmp:
        ans = k
        ans_num = tmp

print(ans)
