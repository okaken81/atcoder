import io
import sys

_INPUT = """\
6 12
2 3
4 6
1 2
4 5
2 6
1 5
4 5
1 3
1 2
2 6
2 3
2 5
5
3 5
1 4
2 6
4 6
5 6

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

import itertools

n, m = map(int, input().split())
ab = [0] * m

for i in range(m):
    ab[i] = list(map(int, input().split()))

k = int(input())

cd = [0] * k

for i in range(k):
    cd[i] = list(map(int, input().split()))

ans = 0

for v in itertools.product([0, 1], repeat=k):
    joken = set()
    for i in range(k):
        joken.add(cd[i][v[i]])
    tmp = 0
    for i in range(m):
        if set(ab[i]).issubset(joken):
            tmp += 1
    if tmp > ans:
        ans = tmp

print(ans)







