import io
import sys

_INPUT = """\
3 1
1 2 3
4 5 6
7 8 9
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, K = map(int, input().split())
    if N == 1:
        print(input())
        exit()
    A = [list(map(int, input().split())) for _ in range(N)]
    ans_list = sum(A, [])
    ans_list.sort()
    if K == 1:
        print(ans_list[0])
        exit()
    l = 0
    r = N**2
    while r-l > 1:
        c = (r+l)//2
        A_bool = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                A_bool[i][j] = int(A[i][j] > ans_list[c])
        for i in range(N):
            for j in range(N):
                if i:
                    A_bool[i][j] += A_bool[i-1][j]
        for i in range(N):
            for j in range(N):
                if j:
                    A_bool[i][j] += A_bool[i][j-1]
        for i in range(N-K+1):
            for j in range(N-K+1):
                bool_sum = A_bool[i+K-1][j+K-1]
                if i:
                    bool_sum -= A_bool[i-1][j+K-1]
                if j:
                    bool_sum -= A_bool[i+K-1][j-1]
                if i and j:
                    bool_sum += A_bool[i-1][j-1]
                if bool_sum >= K**2//2+1:
                    continue
                else:
                    break
            else:
                continue
            break
        else:
            l = c
            continue
        r = c
    print(ans_list[r])
    
if __name__ == '__main__':
    main()