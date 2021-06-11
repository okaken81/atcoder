import io
import sys

_INPUT = """\
3 2
5 5
2 1
2 2

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N, K = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(N)]
    friends.sort()
    a = 0
    for i in range(N):
        if friends[i][0]-a > K:
            break
        else:
            K = K - friends[i][0] + a + friends[i][1]
            a = friends[i][0]
    print(a+K)

if __name__ == '__main__':
    main()