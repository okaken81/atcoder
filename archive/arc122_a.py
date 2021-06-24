import io
import sys

_INPUT = """\
10
866111664 178537096 844917655 218662351 383133839 231371336 353498483 865935868 472381277 579910117

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    if N == 1:
        print(input())
        exit()
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    sum_l = [0] * N
    num_l = [0] * N
    sum_l[0] = A[0]
    num_l[0] = 1
    sum_l[1] = A[0]*2 % mod
    num_l[1] = 2
    for i in range(2, N):
        num_l[i] = (num_l[i-1] + num_l[i-2]) % mod
        sum_l[i] = (sum_l[i-1] + sum_l[i-2]) % mod
        sum_l[i] += (A[i]*num_l[i-1]) % mod
        sum_l[i] += ((A[i-1]-A[i])*num_l[i-2]) % mod
        sum_l[i] %= mod
    print(sum_l[-1])
if __name__ == '__main__':
    main()