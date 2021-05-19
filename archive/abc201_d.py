import io
import sys

_INPUT = """\
3 3
---
+-+
+--

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    H, W = map(int, input().split())
    A = [''] * H


if __name__ == '__main__':
    main()