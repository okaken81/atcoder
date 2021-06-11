import io
import sys

_INPUT = """\
4
0 0
0 0
1 0
0 1

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    XY = [list(map(int, input().split())) + [i] for i in range(N)]
    XY.sort()
    ans_list = XY[:2] + XY[-2:]
    XY.sort(key=lambda x:x[1])
    for i in [0,1,-2,-1]:
        if XY[i] in ans_list:
            continue
        else:
            ans_list.append(XY[i])
    ans = []
    for i in range(len(ans_list)-1):
        for j in range(i+1, len(ans_list)):
            ans.append(max(abs(ans_list[i][0]-ans_list[j][0]), abs(ans_list[i][1]-ans_list[j][1])))
    ans.sort(reverse=True)
    print(ans[1])
if __name__ == '__main__':
    main()