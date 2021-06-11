import io
import sys

_INPUT = """\
5
24 11 8 3 16

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    bad_set = set()
    for i in range(N-1):
        if A[i] in bad_set:
            continue
        if A[i] == A[i+1]:
            bad_set.add(A[i])
        j = 2
        while A[i]*j <= A[-1]:
            bad_set.add(A[i]*j)
            j += 1
    A = set(A) - bad_set
    print(len(A))
if __name__ == '__main__':
    main()