import io
import sys

_INPUT = """\
4 4 2 2
##..
...#
#.#.
.#.#

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

h, w, x, y = map(int, input().split())

s = [''] * h

for i in range(h):
    s[i] = list(input())

ans = 1

for i in range(1,x):
    if s[x-i-1][y-1] == '.':
        ans += 1
    else:
        break

for i in range(x,h):
    if s[i][y-1] == '.':
        ans += 1
    else:
        break

for i in range(1,y):
    if s[x-1][y-i-1] == '.':
        ans += 1
    else:
        break

for i in range(y,w):
    if s[x-1][i] == '.':
        ans += 1
    else:
        break

print(ans)









