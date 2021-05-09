import io
import sys

_INPUT = """\
2
4 3

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    from itertools import product

    N = int(input())
    X = list(map(int, input().split()))

    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    prime_n = len(prime)

    ans = 614889782588491410

    for v in product([0,1], repeat=prime_n):
        divisor = [prime[i] for i in range(prime_n) if v[i] == 1]
        if not divisor: continue
        ans_tmp = 1
        for i in divisor:
            ans_tmp *= i
        if ans_tmp < ans:
            for x in X:
                for d in divisor:
                    if x % d == 0: break
                else: break
            else: ans = ans_tmp

    print(ans) 

main()