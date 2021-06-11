import io
import sys

_INPUT = """\
10460353208

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():
    N = int(input())
    a = 1
    while 3**a < N:
        b = 1
        while 3**a + 5**b <= N:
            if 3**a + 5**b == N:
                print(a,b)
                exit()
            b += 1
        a += 1
    print(-1)
main()