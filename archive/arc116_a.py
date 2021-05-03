import io
import sys

_INPUT = """\
3
2
998244353
1000000000000000000

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        if N % 4 == 0:
            print('Even')
        elif N % 2 == 0:
            print('Same')
        else:
            print('Odd')

main()