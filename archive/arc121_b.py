import io
import sys

_INPUT = """\
1
1 R
2 G

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
  N = int(input())
  dog = []
  r = g = b = 0
  for _ in range(N*2):
    a, c = input().split()
    if c == 'R':
      r = 1 - r
    elif c == 'G':
      g = 1 - g
    else:
      b = 1 - b
    dog.append([int(a), c])
  if r == 0 and g == 0:
    print(0)
    exit()
  dog.sort()
  RG = GB = BR = 10 ** 15
  for i in range(N*2-1):
    if (dog[i][1] == 'R' and dog[i+1][1] == 'G') or (dog[i][1] == 'G' and dog[i+1][1] == 'R'):
      tmp = abs(dog[i][0] - dog[i+1][0])
      if tmp < RG:
        RG = tmp
    elif (dog[i][1] == 'G' and dog[i+1][1] == 'B') or (dog[i][1] == 'B' and dog[i+1][1] == 'G'):
      tmp = abs(dog[i][0] - dog[i+1][0])
      if tmp < GB:
        GB = tmp
    elif (dog[i][1] == 'B' and dog[i+1][1] == 'R') or (dog[i][1] == 'R' and dog[i+1][1] == 'B'):
      tmp = abs(dog[i][0] - dog[i+1][0])
      if tmp < BR:
        BR = tmp
  if r == 1 and g == 1:
    print(min(RG, GB+BR))
  elif g == 1 and b == 1:
    print(min(GB, BR+RG))
  elif b == 1 and r == 1:
    print(min(BR, RG+GB))
main()