import io
import sys

_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, A, B = map(int, input().split())

    print(N-A+B)

main()