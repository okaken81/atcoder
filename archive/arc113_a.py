import io
import sys

_INPUT = """\
200000
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    K = int(input())

    ans = 0

    for i in range(1,K+1):
        for j in range(1,K+1):
            k = i*j
            if k > K:
                break
            ans += K // k
    
    print(ans)

if __name__ == '__main__':
    main()