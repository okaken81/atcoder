import io
import sys

_INPUT = """\
50 0

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    A, B = map(int, input().split())
    print(A*B/100)

if __name__ == '__main__':
    main()