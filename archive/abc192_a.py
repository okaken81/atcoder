import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
    readline = sys.stdin.readline

    x = int(readline())

    print(100 - x % 100)

main()