import io
import sys

_INPUT = """\
4
1 2
1 3
4 2
2 3

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
    readline = sys.stdin.readline

    N = int(readline())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(A)

if __name__ == '__main__':
    main()