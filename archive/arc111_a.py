import io
import sys

_INPUT = """\
1000000000000000000 9997
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

N, M = map(int, input().split())
print(pow(10, N, M*M) // M % M)