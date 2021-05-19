import io
import sys

_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, M = map(int, input().split())

    r = [M]

    for i in range(2,N+1):
        num = 10


if __name__ == '__main__':
    main()