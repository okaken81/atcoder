import io
import sys

_INPUT = """\
3
10 10 10

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 

    readline = sys.stdin.readline

    N = int(readline())
    A = list(map(int, readline().split()))

    list_j = range(N-1)
    ans = 2 ** 31

    for i in range(2 ** (N-1)):
        a = A[0]
        xor = 0
        for j in list_j:
            if(i >> j) & 1:
                xor ^= a
                a = A[j+1]
            else:
                a |= A[j+1]
        xor ^= a
        if xor < ans:
            ans = xor
        
    print(ans)

main()







