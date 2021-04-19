import io
import sys

_INPUT = """\
6
5 3
7 4

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    import sys
    import math
    from builtins import map, int, list, range 

    readline = sys.stdin.readline

    n = int(readline())
    x0, y0 = map(int, readline().split())
    xn2, yn2 = map(int, readline().split())
    xc = (x0+xn2)/2
    yc = (y0+yn2)/2
    length = math.sqrt((x0-xc)**2 + (y0-yc)**2)
    angle = math.degrees(math.acos((y0-yc)/length))
    if x0 > xc:
        angle = -angle
    sinx = math.sin(math.radians(angle + 360/n)) * length
    cosx = math.cos(math.radians(angle + 360/n)) * length

    xn = xc - sinx
    yn = yc + cosx

    print(xn, yn)

main()
