import io
import sys

_INPUT = """\
1 1000000000000000000 10 1000000000

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import math
    X, Y, A, B = map(int, input().split())
    n = 0
    while X * (A-1) < B and X*A < Y:
        X *= A
        n += 1
    ans = (Y-X)//B + n
    if X + B*(ans-n) >= Y:
        ans -= 1
    print(ans)
if __name__ == '__main__':
    main()