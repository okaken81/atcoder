import io
import sys

_INPUT = """\
2
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
 
    readline = sys.stdin.readline

    n = int(readline())

    print(n-1)

main()