import io
import sys

_INPUT = """\
5
OR
OR
OR
OR
OR

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())

    ans = 1

    for i in range(N):
        S = input()
        if S == 'OR':
            ans += 2**(i+1)

    print(ans)

main()