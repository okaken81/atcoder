import io
import sys

_INPUT = """\
3 3
B..
RRB
BBB
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    color = 0
    for n in range(H+W-1):
        if H-1 < n:
            i_max = H-1
        else:
            i_max = n
        if W-1 < n:
            j_max = W-1
        else:
            j_max = n
        s = S[n-j_max][j_max]
        cnt = 0
        num_dot = 0
        for i in range(i_max+1):
            j = n-i
            if j_max < j:
                continue
            elif s != '.' and s != S[i][j] and S[i][j] != '.':
                print(0)
                exit()
            elif s == '.' and s != S[i][j]:
                s = S[i][j]
            elif s == '.' and S[i][j] == '.':
                num_dot += 1
            cnt += 1
        if cnt == num_dot:
            color += 1
    print(pow(2, color, 998244353))
if __name__ == '__main__':
    main()