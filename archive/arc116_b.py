import io
import sys

_INPUT = """\
7
853983 14095 543053 143209 4324 524361 45154

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    mod = 998244353

    ans = 0
    sum_min = 0

    for i in range(N):
        ans += A[i] * A[i]
        ans += sum_min * A[i]
        sum_min = (sum_min * 2 + A[i]) % mod
        ans %= mod
    
    print(ans)

main()