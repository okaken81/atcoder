import io
import sys

_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())

    i = 1
    D = []

    while i*i <= N:
        if N % i == 0:
            print(i)
            d = N // i
            if d != i:
                D.append(d)
        i += 1
    
    for d in D[::-1]:
        print(d)

main()