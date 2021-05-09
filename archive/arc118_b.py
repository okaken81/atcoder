import io
import sys

_INPUT = """\
3 10 5
2 3 5
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    K, N, M = map(int, input().split())
    A = list(map(int, input().split()))

    B = [M*a//N for a in A]

    A_B = [[i, (A[i]*M - B[i]*N)/M/N] for i in range(K)]

    A_B.sort(key=lambda x: x[1], reverse=True)

    for i in range(M - sum(B)):
        B[A_B[i][0]] += 1
    
    print(' '.join([str(b) for b in B]))

main()