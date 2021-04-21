import io
import sys

_INPUT = """\
99999 99998
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

a, b = map(int, input().split())

print((a - b) / a * 100)

















