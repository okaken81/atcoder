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
    import sys
    from builtins import map, int, list, range, dict, zip, str
    from itertools import permutations

    s1 = list(input())
    s2 = list(input())
    s3 = list(input())

    all_str = set(s1 + s2 + s3)

    if len(all_str) > 10:
        print('UNSOLVABLE')
        exit()
    
    numbers = [str(i) for i in range(10)]

    for v in permutations(numbers, len(all_str)):
        d_str = dict(zip(all_str, v))
        n1 = [d_str[s1[i]] for i in range(len(s1))]
        n2 = [d_str[s2[i]] for i in range(len(s2))]
        n3 = [d_str[s3[i]] for i in range(len(s3))]

        if n1[0] == '0' or n2[0] == '0' or n3[0] == '0':
            continue

        n1 = int(''.join(n1))
        n2 = int(''.join(n2))
        n3 = int(''.join(n3))

        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            exit()
        
    print('UNSOLVABLE')

main()