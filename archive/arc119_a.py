import io
import sys

_INPUT = """\
998984374864432412

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import math

    N = int(input())
    n = int(math.log(N,2))

    ans = 10**18

    for b in range(n+1):
        a = N // (2**b)
        c = N - a*2**b
        if a+b+c < ans:
            ans = a+b+c

    print(ans)

if __name__ == '__main__':
    main()