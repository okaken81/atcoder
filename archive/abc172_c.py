import io
import sys

_INPUT = """\
3 4 730
60 90 120
80 150 80 150

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    times = 0
    books = 0
    for ai in range(N):
        times += A[ai]
        if times > K:
            times -= A[ai]
            ai -= 1
            break
        books += 1
    bi = 0
    ans = books
    while True:
        while bi < M and times + B[bi] <= K:
            times += B[bi]
            books += 1
            bi += 1
        if books > ans:
            ans = books
        if bi >= M-1:
            break
        if ai < 0:
            break
        books -= 1
        times -= A[ai]
        ai -= 1
    print(ans)
if __name__ == '__main__':
    main()