import io
import sys

_INPUT = """\
5 5
.....
.###.
.###.
.###.
.....

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
    readline = sys.stdin.readline

    H, W = map(int, input().split())

    ans = 0

    for i in range(H):
        if i > 0:
            line = line_under
        line_under = list(readline())[:-1]
        if i > 0:
            for j in range(W-1):
                black = 0
                if line[j] == '#':
                    black += 1
                if line[j+1] == '#':
                    black += 1
                if line_under[j] == '#':
                    black += 1
                if line_under[j+1] == '#':
                    black += 1
                if black == 1 or black == 3:
                    ans += 1
    print(ans)

main()