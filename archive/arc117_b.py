import io
import sys

_INPUT = """\
7
314 159 265 358 979 323 846
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    N = int(input())
    A = set(map(int, input().split()))
    A = list(A)
    A.sort()

    A = [A[0]] + [A[i] - A[i-1] for i in range(1,len(A))]

    ans = 1

    for i in range(len(A)):
        ans *= A[i] + 1
        ans %= 10**9 + 7
    
    print(ans)

main()