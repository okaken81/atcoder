import io
import sys

_INPUT = """\
27182818284590

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

n = int(input())

ans = 0

if n >= 10**3: ans += n - 10**3 + 1
if n >= 10**6: ans += n - 10**6 + 1
if n >= 10**9: ans += n - 10**9 + 1
if n >= 10**12: ans += n - 10**12 + 1
if n >= 10**15: ans += n - 10**15 + 1

print(ans)









