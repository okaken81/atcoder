import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    a = int(input())

    print(a + a**2 + a**3)

if __name__ == '__main__':
    main()