import io
import sys

_INPUT = """\
5 5
.....
.###.
.###.
.###.
.....

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
    readline = sys.stdin.readline

    H, W = map(int, input().split())

main()