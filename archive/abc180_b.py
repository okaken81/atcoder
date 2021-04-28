import io
import sys

_INPUT = """\
10
3 -1 -4 1 -5 9 2 -6 5 -3
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import math
    N = int(input())
    X = list(map(int, input().split()))

    print(sum([abs(x) for x in X]))
    print(math.sqrt(sum(x ** 2 for x in X)))
    print(max([abs(x) for x in X]))

main()