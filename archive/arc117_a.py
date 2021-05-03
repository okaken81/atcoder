import io
import sys

_INPUT = """\
100 300

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a
        r = 1
    else:
        r = 0
    
    B = list(range(1, b+1))
    A_max = sum(B[-(b-a+1):])
    A = list(range(1, a)) + [A_max]

    if r == 1:
        A = [-i for i in A]
    else:
        B = [-i for i in B]

    print(' '.join(
        [str(i) for i in A + B]
    ))

main()