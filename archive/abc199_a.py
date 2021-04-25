import io
import sys

_INPUT = """\
3 4 5
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
 
    readline = sys.stdin.readline

    a, b, c = map(int, readline().split())

    if a ** 2 + b ** 2 < c ** 2:
        print('Yes')
    else:
        print('No')

main()