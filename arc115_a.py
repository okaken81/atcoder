import io
import sys

_INPUT = """\
7 5
10101
00001
00110
11110
00100
11111
10000

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range, sum
    readline = sys.stdin.readline

    N, M = map(int, readline().split())

    odd = 0
    even = 0

    for _ in range(N):
        S = map(int, list(readline())[:-1])
        if sum(S) % 2 == 0:
            even += 1
        else:
            odd += 1
    
    print(odd * even)

main()