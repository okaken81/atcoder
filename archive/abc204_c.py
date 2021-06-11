import io
import sys

_INPUT = """\
3 0

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, M = map(int, input().split())
    AB = [[0] * N for _ in range(N)]
    for i in range(N):
        AB[i][i] = 1
    for _ in range(M):
        a, b = map(int, input().split())
        AB[a-1][b-1] = 1
        i_list = []
        for i in range(N):
            if AB[i][a-1] == 1 and AB[i][b-1] == 0:
                AB[i][b-1] = 1
                i_list.append(i)
        for i in range(N):
            if AB[b-1][i] == 1 and AB[a-1][i] == 0:
                AB[a-1][i] = 1
                for j in i_list:
                    AB[j][i] = 1
    print(sum(sum(AB, [])))
if __name__ == '__main__':
    main()