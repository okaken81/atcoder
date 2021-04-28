import io
import sys

_INPUT = """\
-9 99 -999 9999

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    sx, sy, gx, gy = map(int, input().split())

    print(sx + (gx - sx) * sy / (sy + gy))

main()