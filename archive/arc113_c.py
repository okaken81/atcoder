import io
import sys

_INPUT = """\
anerroroccurred

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    S = input()
    S = S[::-1]
    i_before = 0
    ans = 0

    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans += i - S[i_before:i].count(S[i])
            if S[i_before] == S[i]:
                ans -= i_before
            i_before = i
                
    print(ans)

if __name__ == '__main__':
    main()