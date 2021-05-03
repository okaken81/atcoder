import io
import sys

_INPUT = """\
10
6 7 5 18 2
3 8 1 6 3
7 2 8 7 7
6 3 3 4 7
12 8 9 15 9
9 8 6 1 10
12 9 7 8 2
10 3 17 4 10
3 1 3 19 3
3 14 7 13 1

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = [tuple(map(int, input().split())) for i in range(N)]

    def check(x):
        s = set()
        for a in A:
            s.add(sum(1 << i for i in range(5) if a[i] >= x))
        
        for x in s:
            for y in s:
                for z in s:
                    if x | y | z == 31:
                        return True
        return False
    
    ok = 0
    ng = 10**9 + 1

    while ng - ok > 1:
        cen = (ok + ng) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen
            
    print(ok) 

main()