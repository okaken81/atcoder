import io
import sys

_INPUT = """\
1 1
2
10
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for _ in range(Q):
        k = int(input())
        if k < A[0]:
            print(k)
        elif k+N > A[-1]:
            print(k+N)
        else:
            l = 0
            r = N-1
            while r-l>1:
                c = (r+l)//2
                if A[c] < k+c+1:
                    l = c
                else:
                    r = c
            print(k+l+1)
if __name__ == '__main__':
    main()