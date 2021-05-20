import io
import sys

_INPUT = """\
4
20 11 9 24

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))
xor = 0
for a in A:
    xor ^= a
for i in range(N):
    A[i] ^= xor
print(*A)