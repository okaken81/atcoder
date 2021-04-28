import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    x = int(input())

    if x >= 0:
        print(x)
    else:
        print(0)

main()