import io
import sys

_INPUT = """\
2
-199 1000
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    if N == 1:
        print(max(0, int(input())))
        exit()
    A = list(map(int, input().split()))
    A2 = [0]*N
    A3 = [0]*N
    A2[0] = A[0]
    A3[0] = A[0]
    A2_max = 0
    ans = 0
    for i in range(N-1):
        if i:
            A2[i] = A[i] + A2[i-1]
            A3[i] = A2[i] + A3[i-1]
        if A2[i] > A2_max:
            A2_max = A2[i]
        if A2_max + A3[i] > ans:
            ans = A2_max + A3[i]
    A2[-1] = A[-1] + A2[-2]
    A3[-1] = A2[-1] + A3[-2]
    if A3[-1] > ans:
        ans = A3[-1]
    print(ans)
if __name__ == '__main__':
    main()