import io
import sys

_INPUT = """\
3 3
1 2
2 3
3 1
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
 
    readline = sys.stdin.readline

    N, M = map(int, input().split())


main()