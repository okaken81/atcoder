import io
import sys

_INPUT = """\
4
1 2 3 2

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    a_max = 0
    a_max2 = 0
    a_sum = 0
    for i in range(N):
        if A[i] > a_max:
            a_max2 += A[i]*2 - a_max
            a_sum += i * (A[i]-a_max) + a_max2
            a_max = A[i]
            print(a_sum)
        else:
            a_max2 += A[i]
            a_sum += a_max2
            print(a_sum)
if __name__ == '__main__':
    main()