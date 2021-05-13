import io
import sys

_INPUT = """\
3141592 6535897 9323846

"""
sys.stdin = io.StringIO(_INPUT)

# ----------------------------------------------------------

def main():
    a, b, c = map(int, input().split())
    
    a_tail = int(str(a)[-1])
    a_tail_tmp = a_tail
    a_tail_list = []

    for i in range(10):
        a_tail_list.append(a_tail_tmp)
        a_tail_tmp = int(str(a_tail_tmp * a_tail)[-1])
        if a_tail_tmp == a_tail:
            break
    
    if len(a_tail_list) == 1:
        print(a_tail_list[0])
        exit()
    elif len(a_tail_list) == 2:
        if b % 2 == 0:
            print(a_tail_list[-1])
            exit()
        else:
            print(a_tail_list[0])
            exit()

    if b < 10:
        b_tail = b
    else:
        b_tail = int(str(b)[-2:])

    b_tail_tmp = b_tail
    b_tail_list = []

    for i in range(100):
        b_tail_list.append(b_tail_tmp)
        b_tail_tmp = int(str(b_tail_tmp * b_tail)[-2:])
        if b_tail_tmp == b_tail:
            break
    
    bc = b_tail_list[(c-1) % len(b_tail_list)]

    print(a_tail_list[(bc-1) % len(a_tail_list)])

if __name__ == '__main__':
    main()