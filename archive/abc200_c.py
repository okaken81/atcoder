import io
import sys

_INPUT = """\
6
123 223 123 523 200 2000
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 

    N = int(input())
    A = list(map(int, input().split()))

    A = [a % 200 for a in A]

    ans = 0

    for i in range(0, 200):
        same = 0
        for a in A:
            if a == i:
                same += 1
        if same > 1:
            ans += same * (same-1) // 2

    print(ans)

main()