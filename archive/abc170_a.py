import io
import sys

_INPUT = """\
1 2 0 4 5

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

X = list(map(int, input().split()))
print(X.index(0)+1)