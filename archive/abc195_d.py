import io
import sys

_INPUT = """\
3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

n, m, q = map(int, input().split())

wv = [0] * n

for i in range(n):
    wv[i] = list(map(int, input().split()))

wv.sort(reverse=True, key=lambda x: x[1])

x = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    x_tmp = x[:l-1] + x[r:]
    x_len = len(x_tmp)
    if x_len == 0:
        print(0)
        continue
    x_tmp.sort()
    ans = 0
    for i in range(n):
        if x_len == 0:
            break
        for j in range(x_len):
            if wv[i][0] <= x_tmp[j]:
                ans += wv[i][1]
                del x_tmp[j]
                x_len = len(x_tmp)
                break
    print(ans)











