import io
import sys

_INPUT = """\
1 10 10
3 2


"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, D, H = map(int, input().split())

    ans = 0

    for _ in range(N):
        d, h = map(int, input().split())
        high = H - (H - h) / (D - d) * D
        if high < 0:
            high = 0
        if high > ans:
            ans = high
    
    print(ans)

main()