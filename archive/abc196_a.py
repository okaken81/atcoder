import io
import sys

_INPUT = """\
0 10
0 10
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 

    readline = sys.stdin.readline

    a, b = map(int, readline().split())
    c, d = map(int, readline().split())

    print(b-c)

main()











