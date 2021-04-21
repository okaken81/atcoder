import io
import sys

_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

n = int(input())

a_max = 100000
b_max = 33

ab = set() 

for a in range(1, a_max):
    for b in range(1, b_max):
        if (a+1) ** (b+1) <= n:
            ab.add((a+1) ** (b+1))
        else:
            break

print(n-len(ab))













