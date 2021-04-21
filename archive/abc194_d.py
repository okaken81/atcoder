import io
import sys

_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

n = int(input())

ans = 0

for i in range(1, n):
    ans += n / (n - i)

print(ans)















