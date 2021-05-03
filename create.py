
def main():
    import os
    import shutil

    main_title = 'zone2021'
    sub_title = ['a', 'b', 'c', 'd', 'e', 'f']
    # sub_title = ['d']

    dir = './atcoder/'

    for st in sub_title:
        if os.path.isfile(dir + main_title + '_' + st + '.py'):
            print(main_title + '_' + st + '.py exists')
        elif os.path.isfile(dir + 'archive/' + main_title + '_' + st + '.py'):
            print(main_title + '_' + st + '.py exists in archive')
        else:
            shutil.copyfile(dir + 'format.py', dir + main_title + '_' + st + '.py')
            print(main_title + '_' + st + '.py created')

main()