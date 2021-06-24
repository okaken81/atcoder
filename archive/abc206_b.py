import io
import sys

_INPUT = """\
1
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    i = 0
    m = 0
    while m < N:
        i += 1
        m += i
    print(i)

if __name__ == '__main__':
    main()