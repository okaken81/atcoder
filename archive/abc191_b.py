import io
import sys

_INPUT = """\
3 3
3 3 3
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    print(' '.join([str(a) for a in A if a != X]))

main()