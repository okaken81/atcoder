import io
import sys

_INPUT = """\
ZONeZONeZONe

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

print(input().count('ZONe'))