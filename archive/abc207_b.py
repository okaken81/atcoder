import io
import sys

_INPUT = """\
6 9 2 3

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import math
    A, B, C, D = map(int, input().split())
    if C * D <= B:
        print(-1)
    else:
        print(math.ceil(A / (C*D-B)))
if __name__ == '__main__':
    main()