import io
import sys

_INPUT = """\
hellospaceRhellospace
"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():

    from collections import deque

    S = list(input())
    T = deque()
    len_S = 0
    r = 0

    for i in range(len(S)):
        if S[i] == 'R':
            r = 1 - r
        else:
            if len_S < 2:
                r = 0
            if r == 0:
                if len_S > 0:
                    if T[-1] == S[i]:
                        T.pop()
                        len_S -= 1
                        continue
                T.append(S[i])
                len_S += 1
            else:
                if len_S > 0:
                    if T[0] == S[i]:
                        T.popleft()
                        len_S -= 1
                        continue
                T.appendleft(S[i])
                len_S += 1
        
    
    if r == 1:
        T.reverse()
    
    print(''.join(T))

main()