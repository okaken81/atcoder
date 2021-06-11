import io
import sys

_INPUT = """\
5 6 4

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    a, b, c = map(int, input().split())
    print(21-a-b-c)
if __name__ == '__main__':
    main()