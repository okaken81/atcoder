import io
import sys

_INPUT = """\
10 1

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    B, C = map(int, input().split())

    if C == 1:
        if B == 0:
            print(1)
            exit()
        else:
            print(2)
            exit()

    ans = C//2 + (C-1)//2*2 + (C-2)//2 + 2

    if B > 0:
        if (C-1)//2 >= B:
            ans -= (C-1)//2-B + C//2-B + 1
    else:
        if (C-2)//2 >= -B:
            ans -= (C-2)//2+B + (C-1)//2+B + 1
    
    print(ans)


if __name__ == '__main__':
    main()