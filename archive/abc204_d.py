import io
import sys

_INPUT = """\
5
8 3 7 2 5

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    T = list(map(int, input().split()))
    print(2**100)

if __name__ == '__main__':
    main()