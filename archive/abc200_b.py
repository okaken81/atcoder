import io
import sys

_INPUT = """\
8691 20

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    N, K = map(int, input().split())

    for _ in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = N * 1000 + 200
    
    print(N)

main()