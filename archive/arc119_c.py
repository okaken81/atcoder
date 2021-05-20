import io
import sys

_INPUT = """\
14
630551244 683685976 249199599 863395255 667330388 617766025 564631293 614195656 944865979 277535591 390222868 527065404 136842536 971731491

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import numpy as np
    N = int(input())
    A = np.array(input().split(), np.int64)
    A[::2] *= -1
    A_cum = np.append(0, np.cumsum(A))
    count = {}
    ans = 0
    for x in A_cum:
        ans += count.get(x,0)
        count[x] = count.get(x,0) + 1
    return ans

if __name__ == '__main__':
    print(main())