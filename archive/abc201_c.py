import io
import sys

_INPUT = """\
xxxxx?xxxo

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    S = input()

    must = 0
    may = 0

    for i in range(10):
        if S[i] == 'o':
            must += 1
        elif S[i] == '?':
            may += 1

    if must > 4:
        print(0)
    elif must == 4:
        print(4*3*2*1)
    elif must == 3:
        print(4*3*3 + 4*3*2*may)
    elif must == 2:
        print(2**4-2 + 4*(2**3-2)*may + 6*2*may**2)
    elif must == 1:
        print(1 + 4*may + 6*may**2 + 4*may**3)
    else:
        print(may**4)

if __name__ == '__main__':
    main()