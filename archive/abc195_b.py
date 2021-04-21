import io
import sys

_INPUT = """\
300 333 1

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

a, b, w = map(int, input().split())

w = w * 1000
min = w // b
max = w // a
min_ans = 0
max_ans = 0

for i in range(min, max+1):
    if w / i <= b and w / i >= a:
        max_ans = i
        if min_ans == 0:
            min_ans = i
            
if min_ans == 0:
    print('UNSATISFIABLE')
else:
    print(min_ans, max_ans)










