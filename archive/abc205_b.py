import io
import sys

_INPUT = """\
1
1

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A == list(range(1,N+1)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()