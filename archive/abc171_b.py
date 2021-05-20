import io
import sys

_INPUT = """\
1 1
1000

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    P.sort()

    print(sum(P[0:K]))

if __name__ == '__main__':
    main()