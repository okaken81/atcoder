import io
import sys

_INPUT = """\
1 100
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import math

    t, N = map(int, input().split())

    print(math.ceil(N*100/t) * (100+t) //100 - 1)

main()