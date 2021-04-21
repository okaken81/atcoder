import io
import sys

_INPUT = """\
14
5 5
0 1
2 5
8 0
2 1
0 0
3 6
8 6
5 9
7 9
3 4
9 2
9 8
7 2
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

import math

n = int(input())

point = [[] for _ in range(n)]

for i in range(n):
    point[i] = list(map(int, input().split()))

ans = 0

for i in range(n - 2):
    x1 = point[i][0]
    y1 = point[i][1]
    for j in range(i + 1, n - 1):
        x2 = point[j][0]
        y2 = point[j][1]
        x12 = x1 - x2
        y12 = y1 - y2
        gcd12 = math.gcd(x12, y12)
        x12 //= gcd12
        y12 //= gcd12
        if x12 < 0:
            x12 = -x12
            y12 = -y12
        for k in range(j + 1, n):
            x3 = point[k][0]
            y3 = point[k][1]
            x13 = x1 - x3
            y13 = y1 - y3
            if x12 == 0:
                if x13 == 0:
                    ans += 1
            elif y12 == 0:
                if y13 == 0:
                    ans += 1
            else:
                gcd13 = math.gcd(x13, y13)
                x13 //= gcd13
                y13 //= gcd13
                if x13 < 0:
                    x13 = -x13
                    y13 = -y13
                if x12 == x13:
                    if y12 == y13:
                        ans += 1
            if ans == 1:
                break
        if ans == 1:
            break
    if ans == 1:
        break

if ans == 0:
    print('No')
else:
    print('Yes')