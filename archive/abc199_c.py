import io
import sys

_INPUT = """\
2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
 
    readline = sys.stdin.readline

    N = int(input())
    S = list(input())
    Q = int(input())

    exchange = 0

    for _ in range(Q):
        T, A, B = map(int, readline().split())

        if T == 1:
            if exchange == 1:
                if A > N:
                    A -= N
                else:
                    A += N
                if B > N:
                    B -= N
                else:
                    B += N
            S[A-1], S[B-1] = S[B-1], S[A-1]
        if T == 2:
            exchange = 1 - exchange

    if exchange == 1:
        S[0:N], S[N:N*2] = S[N:N*2], S[0:N]

    return print(''.join(S))

main()