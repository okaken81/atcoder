import io
import sys

_INPUT = """\
2
-3 6
4 2
"""
sys.stdin = io.StringIO(_INPUT)

# import numpy as np
# import pandas as pd
# import math
# import itertools
# import collections

# a = list(map(int, input().split()))
# n = int(input())
# d, t, s = map(int, input().split())

#### ----------------------------------

import numpy as np

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if np.dot(a, b) == 0:
    print('Yes')
else:
    print('No')