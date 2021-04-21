import io
import sys

_INPUT = """\
1120

"""
sys.stdin = io.StringIO(_INPUT)

#### ----------------------------------

def main():
    from builtins import map, int, list, range, input
 
    N = list(input())

    if len(N) == 1:
        print('Yes')
        exit()

    zero = 0

    for i in range(len(N)):
        if N[-(i+1)] == '0':
            zero += 1
        else:
            break
    
    for _ in range(zero):
        N.insert(0, '0')
    
    for i in range(len(N) // 2):
        if N[i] != N[-(i+1)]:
            i -= 1
            break

    if i == len(N) // 2 - 1:
        print('Yes')
    else:
        print('No')

main()