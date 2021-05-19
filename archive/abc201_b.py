import io
import sys

_INPUT = """\
4
QCFium 2846
chokudai 2992
kyoprofriends 2432
penguinman 2390

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())

    M = [input().split() for _ in range(N)]

    print(M)

    # M = [''] * N

    # for i in range(N):
    #     M[i] = input().split()
    #     M[i][1] = int(M[i][1])
    
    # M.sort(key = lambda x: x[1])

    # print(M[-2][0])

if __name__ == '__main__':
    main()