import io
import sys

_INPUT = """\
a
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

if input().islower():
    print('a')
else:
    print('A')