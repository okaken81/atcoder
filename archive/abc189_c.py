import io
import sys

_INPUT = """\
6
200 4 4 9 4 9

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(n):
    m_min = a[i]
    for j in range(i,n):
        if a[j] < m_min:
            m_min = a[j]
        if m_min * (j-i+1) > ans:
            ans = m_min * (j-i+1)
        
print(ans)

















