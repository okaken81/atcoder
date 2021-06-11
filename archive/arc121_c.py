import io
import sys

_INPUT = """\
2
5
2 1 3 5 4
4
4 3 2 1

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        if P == list(range(1,N+1)):
            print(0)
            print()
            continue
        M = 1
        A = []
        while P != list(range(1,N+1)):
            if M % 2 == 1:
                for i in range(N//2):
                    if P[i*2] > P[i*2+1]:
                        P[i*2], P[i*2+1] = P[i*2+1], P[i*2]
                        A.append(i*2+1)
                        break
                else:
                    P[0], P[1] = P[1], P[0]
                    A.append(1)
            if M % 2 == 0:
                for i in range((N-1)//2):
                    if P[i*2+1] > P[i*2+2]:
                        P[i*2+1], P[i*2+2] = P[i*2+2], P[i*2+1]
                        A.append(i*2+2)
                        break
                else:
                    P[1], P[2] = P[2], P[1]
                    A.append(2)
            print(P)
            M += 1
        print(M)
        print(*A)
if __name__ == '__main__':
    main()