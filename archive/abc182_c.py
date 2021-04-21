import io
import sys

_INPUT = """\
14
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

n = list(map(int, input()))
r = sum(n) % 3

if len(n) == 1:
    if r == 0:
        print(0)
    else:
        print(-1)
    exit()

if len(n) == 2:
    if r == 0:
        print(0)
    elif r == 1:
        if any(n[i] % 3 == 1 for i in range(len(n))):
            print(1)
        else:
            print(-1)
    else:
        if any(n[i] % 3 == 2 for i in range(len(n))):
            print(1)
        else:
            print(-1)
    exit()

if r == 0:
    print(0)
elif r == 1:
    if any(n[i] % 3 == 1 for i in range(len(n))):
        print(1)
    elif sum(n[i] % 3 == 2 for i in range(len(n))) >= 2:
        print(2)
    else:
        print(-1)
else:
    if any(n[i] % 3 == 2 for i in range(len(n))):
        print(1)
    elif sum(n[i] % 3 == 1 for i in range(len(n))) >= 2:
        print(2)
    else:
        print(-1)
