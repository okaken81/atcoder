import io
import sys

_INPUT = """\
3 3
1 2
2 3
3 2

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    sys.setrecursionlimit(10000)
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
    def dfs(v):
        if temp[v]: return
        temp[v] = True
        for vv in G[v]: dfs(vv)
    ans = 0
    for i in range(N):
        temp = [False] * N
        dfs(i)
        ans += sum(temp)
    print(ans)
if __name__ == '__main__':
    main()