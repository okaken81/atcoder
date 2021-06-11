import io
import sys

_INPUT = """\
3100

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

print(-int(input())%1000)