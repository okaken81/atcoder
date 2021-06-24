import io
import sys

_INPUT = """\
191

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    N = int(input())
    x = int(N * 1.08)
    if x == 206:
        print('so-so')
    elif x < 206:
        print('Yay!')
    else:
        print(':(')

if __name__ == '__main__':
    main()