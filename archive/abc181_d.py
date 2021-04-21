import io
import sys

_INPUT = """\
5
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

s = list(input())

if len(s) == 1:
    if s[0] == '8':
        print('Yes')
        exit()
    else:
        print('No')
elif len(s) == 2:
    for i in range(2, 13):
        eight = list(str(8*i))
        a = 0
        b = 0
        for j in range(len(s)):
            if a == 0 and s[j] == eight[0]:
                a += 1
            elif b == 0 and s[j] == eight[1]:
                b += 1
            if a == 1 and b == 1:
                print('Yes')
                exit()
    print('No')
else:
    for i in range(13, 125):
        eight = list(str(8*i))
        a = 0
        b = 0
        c = 0
        for j in range(len(s)):
            if a == 0 and s[j] == eight[0]:
                a += 1
            elif b == 0 and s[j] == eight[1]:
                b += 1
            elif c == 0 and s[j] == eight[2]:
                c += 1
            if a == 1 and b == 1 and c == 1:
                print('Yes')
                exit()
    print('No')