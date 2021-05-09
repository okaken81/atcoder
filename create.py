
def main():
    import os
    import shutil

    main_title = 'arc118'
    # sub_title = ['a', 'b', 'c', 'd', 'e', 'f']
    sub_title = ['c']

    dir = './atcoder/'

    for st in sub_title:
        file_name = main_title + '_' + st + '.py'
        if os.path.isfile(dir + file_name):
            print(file_name + ' exists')
        elif os.path.isfile(dir + 'archive/' + file_name):
            print(file_name + ' exists in archive')
        else:
            shutil.copyfile(dir + 'format.py', dir + file_name)
            print(file_name + ' created')

main()