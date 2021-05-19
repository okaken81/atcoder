import io
import sys

_INPUT = """\
119
10101111011101001011111000111111101011110011010111111111111111010111111111111110111111110111110111101111111111110111011
11111111111111111111111111011111101011111011110111110010100101001110111011110111111111110010011111101111111101110111011

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    S = list(input())
    T = list(input())

    if S.count('1') != T.count('1'):
        print(-1)
        exit()

    if S == T:
        print(0)
        exit()

    ans = 0
    s_sum = 0
    t_sum = 0

    for i in range(N):
        s_sum += int(S[i])
        t_sum += int(T[i])
        if s_sum != t_sum:
            if S[i] == '0':
                ans += 1
        elif S[i] == '0' and T[i] == '1':
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()