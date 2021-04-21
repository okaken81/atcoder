import io
import sys

_INPUT = """\
5 15 0
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
    import math
 
    readline = sys.stdin.readline

    R, X, Y = map(int, readline().split())

    D = math.sqrt(X**2 + Y**2)

    ans = D/R

    if ans < 1:
        print(2)
    else:
        print(math.ceil(ans))

main()