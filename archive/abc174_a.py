import io
import sys

_INPUT = """\
25
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

if int(input()) >= 30:
    print('Yes')
else:
    print('No')