import io
import sys

_INPUT = """\
963761198400
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    N = int(input())

    ans = 0
    i = 1

    while i * i <= N:
        if N % i == 0:
            if i % 2 == 1:
                ans += 1
            if i * i == N:
                break
            if (N // i) % 2 == 1:
                ans += 1
        i += 1
    
    i = 1
    
    while i * i <= N * 2:
        if (N * 2) % i == 0:
            if N % i != 0 and i % 2 == 0:
                ans += 1
            if i * i == N * 2:
                break
            q = N * 2 // i
            if N % q != 0 and q % 2 == 0:
                ans += 1
        i += 1
    
    print(ans)

main()