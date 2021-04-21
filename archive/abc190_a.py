import io
import sys

_INPUT = """\
2 1 0
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

a, b, c = map(int, input().split())

if c == 1:
    if b <= a:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if a <= b:
        print('Aoki')
    else:
        print('Takahashi')

















