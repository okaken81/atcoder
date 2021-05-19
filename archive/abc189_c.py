import io
import sys

_INPUT = """\
6
200 4 4 9 4 9

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    for l in range(N):
        o_min = A[l]
        for r in range(l,N):
            if A[r] < o_min:
                o_min = A[r]
            if o_min * (N-l) < ans:
                break
            if ans < o_min * (r-l+1):
                ans = o_min * (r-l+1)
    print(ans)

main()