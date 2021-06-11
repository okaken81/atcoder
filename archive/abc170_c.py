import io
import sys

_INPUT = """\
100 0


"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        exit()
    else:
        P = set(map(int, input().split()))
    num_list = set(range(0,102)) - P
    i = 0
    while True:
        if X-i in num_list:
            print(X-i)
            break
        elif X+i in num_list:
            print(X+i)
            break
        i += 1

if __name__ == '__main__':
    main()