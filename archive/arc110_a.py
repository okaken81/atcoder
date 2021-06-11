import io
import sys

_INPUT = """\
20
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    ans = 1
    for i in range(2,N+1):
        if ans % i != 0:
            tmp_i = i
            tmp_ans = ans
            tmp = 1
            j = 2
            while tmp_i > 1:
                if tmp_i % j == 0:
                    tmp_i //= j
                    if tmp_ans % j == 0:
                        tmp_ans //= j
                    else:
                        tmp *= j
                else:
                    j += 1
            ans *= tmp
    print(ans+1)
main()