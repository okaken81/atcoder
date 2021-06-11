import io
import sys

_INPUT = """\
3 3

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, K = map(int, input().split())
    ans = 0
    for n in range(N):
        for k in range(K):
            ans += (n+1)*100 + (k+1)
    print(ans)
if __name__ == '__main__':
    main()