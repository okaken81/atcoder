import io
import sys

_INPUT = """\
10000000

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    from builtins import map, int, list, range 

    readline = sys.stdin.readline

    n = int(readline())

    ans = 0

    for i in range(1,n):
        str_i = str(i)
        str_i += str_i
        str_i = int(str_i)
        if str_i > n:
            break
        else:
            ans += 1
    print(ans)

main()












