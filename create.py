
def main():
    import os
    import shutil

    main_title = 'abc208'
    # sub_title = ['a', 'b', 'c', 'd', 'e', 'f']
    sub_title = ['d']

    dir = os.path.dirname(__file__)
    arc_dir = os.path.join(dir, 'archive')
    format_file_path = os.path.join(dir, 'format.py')

    for st in sub_title:
        file_name = main_title + '_' + st + '.py'
        file_path = os.path.join(dir, file_name)
        arc_file_path = os.path.join(arc_dir, file_name)
        if os.path.isfile(file_path):
            print(file_name + ' exists')
        elif os.path.isfile(arc_file_path):
            print(file_name + ' exists in archive')
        else:
            shutil.copyfile(format_file_path, file_path)
            print(file_name + ' created')

if __name__ == '__main__':
    main()
