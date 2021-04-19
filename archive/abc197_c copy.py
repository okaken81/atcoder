import io
import sys

_INPUT = """\
3
10 10 10

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))

ans = 2 ** 31

for i in range(2 ** (N-1)):
    a = A[0]
    xor = 0
    for j in range(N-1):
        if(i >> j) & 1:
            xor ^= a
            a = A[j+1]
        else:
            a |= A[j+1]
    xor ^= a
    if xor < ans:
        ans = xor
    
print(2 ** 19 * 18)
print(ans)
