import io
import sys

_INPUT = """\
3
11 7
3 2
6 7

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

n = int(input())

a = [0] * n
b = [0] * n

for i in range(n):
    a[i], b[i] = map(int, input().split())

task = 0
ans = 1000000

for i in range(n):
    for j in range(n):
        if i == j:
            task = a[i] + b[j]
        else:
            task = max(a[i], b[j])
        if task < ans:
            ans = task
        
print(ans)










