import io
import sys

_INPUT = """\
6174 100000
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range, sorted, input
    readline = sys.stdin.readline

    N, K = map(int, input().split())


    for _ in range(K):
        N = list(map(int, list(str(N))))

        g1 = sorted(N, reverse=True)
        g1 = ''.join(map(str, g1))
        g1 = int(g1)

        g2 = sorted(N)
        g2 = ''.join(map(str, g2))
        g2 = int(g2)

        N = g1 - g2

    print(N)

main()