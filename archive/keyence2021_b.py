import io
import sys

_INPUT = """\
1 1
1
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

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if a[0] != 0:
    print(0)
    exit()

ans = 0
number = 0
n_number = 0

for i in range(len(a)):
    if a[i] == number:
        n_number += 1
        if n_number <= k:
            ans += 1
    elif a[i] == number + 1:
        if n_number < k:
            k = n_number
        number = a[i]
        n_number = 1
        ans += 1
    else:
        break

print(ans)