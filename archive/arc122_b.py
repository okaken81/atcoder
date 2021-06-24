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
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0]/2
    sumA = A[0]
    for i in range(1,N):
        if A[i] == A[i-1]:
            sumA += A[i]
            continue
        tmp = ((N-2*i) * A[i]/2 + sumA)/N
        if tmp < ans:
            ans = tmp
        sumA += A[i]
    print(ans)
if __name__ == '__main__':
    main()