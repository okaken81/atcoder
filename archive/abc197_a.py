import io
import sys

_INPUT = """\
abc
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

s = list(input())

print(s[1]+s[2]+s[0])











