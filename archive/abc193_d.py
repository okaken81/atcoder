import io
import sys

_INPUT = """\
100000
3226#
3597#
"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

k = int(input())
s = list(input())
t = list(input())

card = [k] * 9

s = list(map(int, s[:-1]))
t = list(map(int, t[:-1]))

for i in range(4):
    card[s[i]-1] -= 1
    card[t[i]-1] -= 1

c_sum = sum(card)
ans = 0

for i in range(9):
    if card[i] == 0:
        continue
    for j in range(9):
        if card[j] == 0:
            continue
        if i == j and card[i] < 2:
            continue
        if i == j:
            p = card[i] * (card[i]-1)
        else:
            p = card[i] * card[j]
        s_tmp = s + [i+1]
        t_tmp = t + [j+1]
        s_score = 0
        t_score = 0
        for l in range(1,10):
            s_score += l * 10**s_tmp.count(l)
            t_score += l * 10**t_tmp.count(l)
        if s_score > t_score:
            ans += p

print(ans / (c_sum * (c_sum-1)))

















