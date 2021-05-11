import io
import sys

_INPUT = """\
4
141421356 17320508 22360679 244949

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    a_sum = 0

    for i in range(N-1):
        a_sum += A[i]
        ans += a_sum * A[i+1]
        ans %= 10**9 + 7
    
    print(ans)

if __name__ == '__main__':
    main()