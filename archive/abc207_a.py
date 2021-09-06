import io
import sys

_INPUT = """\
6 6 6

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[1]+A[2])
if __name__ == '__main__':
    main()