import io
import sys

_INPUT = """\
1 2

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    X, Y = map(int, input().split())
    for i in range(X+1):
        if Y == i*4 + (X-i)*2:
            print('Yes')
            exit()
    print('No')
if __name__ == '__main__':
    main()