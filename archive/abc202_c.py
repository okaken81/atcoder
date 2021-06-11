import io
import sys

_INPUT = """\
1
1
1
1
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A_list = [0] * N
    B_list = [0] * N
    C_list = [0] * N
    for i in range(N):
        A_list[A[i]-1] += 1
        C_list[C[i]-1] += 1
    for i in range(N):
        B_list[B[i]-1] += C_list[i]
    ans = 0
    for i in range(N):
        ans += A_list[i]*B_list[i]
    print(ans)
if __name__ == '__main__':
    main()