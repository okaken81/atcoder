import io
import sys

_INPUT = """\
200
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import math

    N = int(input())

    print(math.ceil(N / 100))

main()