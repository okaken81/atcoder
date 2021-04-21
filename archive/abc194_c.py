import io
import sys

_INPUT = """\
5
-5 8 9 -4 -3
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

n = int(input())
a = list(map(int, input().split()))

sq = 0
i_sum = 0
ij = 0

for i in range(n):
    sq += a[i] ** 2
    if i >= 1:
        ij += i_sum * a[i]
    i_sum += a[i]

print(sq * (n-1) - 2 * ij)













