import io
import sys

_INPUT = """\
1
100
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 
    readline = sys.stdin.readline

    N = int(readline())

    C = [''] * N
    C_def = [''] * N
    C_min = 10 ** 9 + 1
    A = [0] * N

    for i in range(N):
        C[i] = list(map(int, readline().split()))
        C_def[i] = [C[i][j] - C[i][j-1] for j in range(1, N)]
        if i > 0:
            if C_def[i] != C_def[i-1]:
                print('No')
                exit()
        if C_min > C[i][0]:
            C_min = C[i][0]
            B = C[i]
        A[i] = C[i][0]
    
    print('Yes')
    print(' '. join([str(A[i] - B[0]) for i in range(N)]))
    print(' '. join([str(B[i]) for i in range(N)]))

main()