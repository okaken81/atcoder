import io
import sys

_INPUT = """\
send
more
money

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():

    from itertools import permutations
    S = [input() for _ in range(3)]
    letters = list(set(S[0] + S[1] + S[2]))
    if len(letters) > 10:
        print('UNSOLVABLE')
        exit()
    for i in range(3):
        S[i] = [letters.index(s) for s in S[i]]
    for v in permutations(range(10), len(letters)):
        if v[S[0][0]] == 0 or v[S[1][0]] == 0 or v[S[2][0]] == 0:
            continue
        N = [0] * 3
        for i in range(3):
            for j in range(len(S[i])):
                N[i] += v[S[i][-(j+1)]] * 10 ** j
        if N[0] + N[1] == N[2]:
            print(N[0])
            print(N[1])
            print(N[2])
            exit()

    print('UNSOLVABLE')

main()