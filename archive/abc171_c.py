import io
from string import ascii_lowercase
import sys

_INPUT = """\
123456789

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def base10str(value):
    import string
    letters = string.ascii_lowercase
    base = len(letters)
    if (int((value-1) / base)):
        return base10str(int((value-1) / base)) + letters[(value-1)%base]
    return letters[value - 1]

def main():
    N = int(input())
    print(base10str(N))

if __name__ == '__main__':
    main()