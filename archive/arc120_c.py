import io
import sys

_INPUT = """\
3
1 1 1
1 1 2

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if sum(A) != sum(B):
        print(-1)
        exit()
    elif A == B:
        print(0)
        exit()

if __name__ == '__main__':
    main()