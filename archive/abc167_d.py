import io
import sys

_INPUT = """\
6 10
6 5 2 5 3 2
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    P = [0] * N
    p = 0
    P[0] = p
    F = [False] * N
    F[0] = True
    i = 0

    while i < K:
        p = A[p]-1
        if F[p]:
            break
        else:
            F[p] = True
            i += 1
            P[i] = p

main()