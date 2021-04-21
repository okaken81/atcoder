import io
import sys

_INPUT = """\
2 6
1 2 4
2 2 4

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

n, C = map(int, input().split())

event = []

for i in range(n):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))

event.sort()

ans = 0
fee = 0
t = 0

for x, y in event:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y

print(ans)
