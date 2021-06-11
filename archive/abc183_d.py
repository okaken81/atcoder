import io
import sys

_INPUT = """\
4 10
1 3 5
2 4 4
3 10 6
2 3 1

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, W = map(int, input().split())
    TL = [0] * (2*10**5+1)
    for _ in range(N):
        s, t, p = map(int, input().split())
        TL[s] += p
        TL[t] -= p
    w = 0
    for tl in TL:
        w += tl
        if w > W:
            print('No')
            exit()
    print('Yes')
main()