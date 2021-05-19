import io
import sys

_INPUT = """\
5
2 6
0 0
1000000 1000000
12345 67890
0 1000000

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
    readline = sys.stdin.readline

    T = int(readline())

    for _ in range(T):
        L, R = map(int, readline().split())
        if L*2 > R:
            print(0)
        else:
            n = R - L*2 + 1
            print(n*(n+1)//2)

if __name__ == '__main__':
    main()