import io
import sys

_INPUT = """\
3 4 240
60 90 120
80 150 80 150

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


if __name__ == '__main__':
    main()