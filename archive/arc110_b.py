import io
import sys

_INPUT = """\
1
0
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    T = input()
    if T == '1':
        print(10**10*2)
        exit()
    min_S = '110' * (N//3 + 2)
    ans = 0
    for i in range(len(min_S)-N+1):
        if min_S[i:i+N] == T:
            ans += 1
    if ans == 0:
        print(0)
    else:
        ans += 10**10 - (N//3 +2)
        print(ans)

if __name__ == '__main__':
    main()