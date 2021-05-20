import io
import sys

_INPUT = """\
2
1 2
3
1 100
2 100
100 1000

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    A_sum = sum(A)
    num_list = [0] * (10**5)

    for a in A:
        num_list[a-1] += 1
    
    for _ in range(Q):
        b, c = map(int, input().split())
        A_sum += (c-b) * num_list[b-1]
        num_list[c-1] += num_list[b-1]
        num_list[b-1] = 0
        print(A_sum)

if __name__ == '__main__':
    main()