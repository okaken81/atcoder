import io
import sys

_INPUT = """\
7 100 100
10 11
12 67
192 79
154 197
142 158
20 25
17 108

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

n, s, d = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
        print('yes')
        exit()

print('No')















