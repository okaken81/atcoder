import io
import sys

_INPUT = """\
4
8 9 10 11

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a > 10:
            ans += a - 10
    print(ans)
if __name__ == '__main__':
    main()