import io
import sys

_INPUT = """\
9
3 14 15 9 26 5 35 89 79

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import numpy as np
    N = int(input())
    T = list(map(int, input().split()))
    S = np.sum(T)
    DP = np.zeros(S//2+1, dtype=bool)
    DP[0] = 1
    for i in range(N):
        if T[i] > S//2+1:
            continue
        else:
            DP[T[i]:] |= DP[:-T[i]]
    for i in range(S//2+1):
        if DP[-(i+1)]:
            print(S-S//2+i)
            break

if __name__ == '__main__':
    main()