import io
import sys

_INPUT = """\
-8 6 3

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    A, B, C = map(int, input().split())
    if C % 2 == 0:
        if abs(A) == abs(B):
            print('=')
        elif abs(A) > abs(B):
            print('>')
        else:
            print('<')
    else:
        if A == B:
            print('=')
        elif A < B:
            print('<')
        else:
            print('>')

if __name__ == '__main__':
    main()