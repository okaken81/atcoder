import io
import sys

_INPUT = """\
5.9
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

x = input()

dot = x.find('.')

if dot != -1:
    x = x[:dot]

print(x)



