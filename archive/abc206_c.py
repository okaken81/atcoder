import io
import sys

_INPUT = """\
2
1 2

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        if i:
            if A[i-1]==A[i]:
                ans += p
                continue
        for j in range(i+1,N):
            if A[i]!=A[j]:
                p = N-j
                ans += p
                break
        else:
            p = 0
    print(ans)

if __name__ == '__main__':
    main()