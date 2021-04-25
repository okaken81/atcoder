import io
import sys

_INPUT = """\
3
3 2 5
6 9 8

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():
    N = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    x_min = max(A)
    x_max = min(B)
    
    if x_min > x_max:
        print(0)
    else:
        print(x_max - x_min + 1)
    
main()