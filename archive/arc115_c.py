import io
import sys

_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    import math

    N = int(input())

    A = [0] * N

    a = 1
    count = 0

    for i in range(N):
        if count == 2 ** (a-1):
            a += 1
            count = 1
        else:
            count += 1
        A[i] = a
    
    print(' '.join([str(a) for a in A]))

main()