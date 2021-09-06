import io
import sys

_INPUT = """\
2
10 20
30 40
50 60
70 80

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def position(A, B):
    import math
    if A[0] == B[0]:
        r = 90.
    elif A[1] == B[1]:
        r = 0.
    else:
        r = math.degrees(math.atan(abs(A[1]-B[1]) / abs(A[0]-B[0])))
    return (A[0]-B[0])**2 + (A[1]-B[1])**2, r
def main():
    import statistics
    N = int(input())
    if N == 1:
        print('Yes')
        exit()
    ab = [list(map(int, input().split())) for _ in range(N)]
    cd = [list(map(int, input().split())) for _ in range(N)]
    ab_list = []
    cd_list = []
    ab_r = []
    cd_r = []
    for i in range(N-1):
        for j in range(i+1,N):
            d, r = position(ab[i], ab[j])
            ab_r.append(r)
            ab_list.append([d, r])
            d, r = position(cd[i], cd[j])
            cd_r.append(r)
            cd_list.append([d, r])
    r_deff = statistics.mean(ab_r) - statistics.mean(cd_r)
    for i in range(len(ab_list)):
        ab_list[i][1] -= r_deff
    ab_list.sort()
    ab_list.sort(key=lambda x: x[1])
    cd_list.sort()
    cd_list.sort(key=lambda x: x[1])
    if ab_list == cd_list:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()