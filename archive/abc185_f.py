import io
import sys

_INPUT = """\
3 4
1 2 3
2 1 3
2 2 3
1 2 3
2 2 3
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

n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        a_bin = list(bin(a[x])[2:])
        y_bin = list(bin(y)[2:])

        print(a_bin)
        print(y_bin)

        a_new = ['0'] * max(len(a_bin), len(y_bin))

        if len(a_bin) > len(y_bin):
            a_bin, y_bin = y_bin, a_bin

        for i in range(len(a_bin)):
            if a_bin[-i] != y_bin[-i]:
                a_new[-i] = '1'
        
        for i in range(len(y_bin) - len(a_bin)):
            a_new[i] = y_bin[i]
        
        a_new = ''.join(a_new)
        a_new = int(a_new, 2)
        
        print(a_new)