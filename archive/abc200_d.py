import io
import sys

_INPUT = """\
5
180 186 189 191 218
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    from itertools import product

    N = int(input())
    A = list(map(int, input().split()))

    A = [i % 200 for i in A]

    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] == A[j]:
                print('Yes')
                print(1, i + 1)
                print(1, j + 1)
                exit()

    if len(A) > 7:
        N = 8

    C_list = []
    C_mod_list = []
    
    for v in product([0, 1], repeat=N):
        B = [A[i] for i in range(N) if v[i] == 1]
        if not B: continue
        C_list.append(B)
        B_mod = sum(B) % 200
        if B_mod in C_mod_list:
            print('Yes')
            C = C_list[C_mod_list.index(B_mod)]
            B = [A.index(i) + 1 for i in B]
            C = [A.index(i) + 1 for i in C]
            B.sort()
            C.sort()
            print(
                len(B),
                ' '.join([str(i) for i in B])
            )
            print(
                len(C),
                ' '.join([str(i) for i in C])
            )
            exit()
        else:
            C_mod_list.append(B_mod)

    print('No')

main()