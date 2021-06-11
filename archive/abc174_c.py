import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    K = int(input())
    a = 7
    ans = 1
    while a%K != 0:
        a %= K
        a = a * 10 + 7
        ans += 1
        if ans > K:
            print(-1)
            break
    else:
        print(ans)
if __name__ == '__main__':
    main()