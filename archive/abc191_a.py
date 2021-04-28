import io
import sys

_INPUT = """\
10 3 5 30

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    V, T, S, D = map(int, input().split())

    if D < V * T or D > V * S:
        print('Yes')
    else:
        print('No')

main()