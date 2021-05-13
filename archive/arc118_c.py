import io
import sys

_INPUT = """\
2500
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    N = int(input())

    A = set([6, 10, 15])

    if N == 3:
        print(*A)
        exit()

    for i in [6, 10, 15]:
        for j in range(2, 2000):
            a = i * j
            if a > 10000:
                break
            else:
                A.add(a)
                if len(A) == N:
                    print(*A)
                    exit()

main()