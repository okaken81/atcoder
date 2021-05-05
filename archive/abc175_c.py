import io
import sys

_INPUT = """\
1000000000000000 1000000000000000 1000000000000000
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    X, K, D = map(int, input().split())

    X = abs(X)

    if X > K * D:
        print(X - K * D)
    else:
        k = X // D
        if (K - k) % 2 == 0:
            print(X - k * D)
        else:
            print(abs(X - (k+1) * D))

main()