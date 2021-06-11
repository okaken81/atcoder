import io
import sys

_INPUT = """\
30 30 118264581564861424

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    from math import factorial
    A, B, K = map(int, input().split())
    ans = []
    for _ in range(A+B):
        if A == 0:
            ans.append('b')
        else:
            k = factorial(A-1+B) // (factorial(A-1) * factorial(B))
            if K <= k:
                ans.append('a')
                A -= 1
            else:
                ans.append('b')
                B -= 1
                K -= k
    print(''.join(ans))
if __name__ == '__main__':
    main()