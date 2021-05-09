import io
import sys

_INPUT = """\
2
2 1

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------


def main():
    
    N = int(input())
    F = list(map(int, input().split()))

    group = 0
    yet = []
    one_list = []

    def judge(number):
        new_number = F[number]
        if new_number in one_list:
            group += 1  
            yet.append(new_number)
            return
        elif new_number in yet:
            return
        else:
            one_list.append(new_number)
            yet.append(new_number)
            judge(new_number-1)

    for i in range(N):
        if i+1 in yet:
            continue
        elif F[i] == i+1:
            group += 1
            yet.append(i+1)
        else:
            one_list = [i+1]
            yet.append(i+1)
            judge(i)
    
    print(group)
    print((2 ** group - 1) % 998244353)



main()