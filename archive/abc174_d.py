import io
import sys

_INPUT = """\
8
WRWWRWRR

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    C = input()
    w = 0
    r = 0
    for i in range(N):
        if C[i] == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        print(0)
    else:
        print(C[0:r].count('W'))

if __name__ == '__main__':
    main()