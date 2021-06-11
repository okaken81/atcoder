import io
import sys

_INPUT = """\
0 1

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    x, y = map(int, input().split())

    if x == y:
        print(x)
    else:
        print(3-x-y)

if __name__ == '__main__':
    main()