import io
import sys

_INPUT = """\
6

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    S = input()
    S = S[::-1]
    S_list = []
    for i in range(len(S)):
        if S[i] == '6':
            S_list.append('9')
        elif S[i] == '9':
            S_list.append('6')
        else:
            S_list.append(S[i])
    print(''.join(S_list))
if __name__ == '__main__':
    main()