import io
import sys

_INPUT = """\
EaSy
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range, input
    readline = sys.stdin.readline

    s = list(input())

    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].isupper():
                print('No')
                exit()
        if i % 2 == 1:
            if s[i].islower():
                print('No')
                exit()
    print('Yes')

main()