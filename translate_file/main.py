from pprint import pprint
from file_system import Triple_file_extension
import os

# ru - russian en - english


def main():
    for (dir_path, dir_names, file_names) in os.walk('D:/курсы/Python/[11-2021] 100-days-of-code/16 Day 16  - Intermediate - Object Oriented Programming (OOP)'):
        if file_names:
            path_file = '/'.join(os.path.split(dir_path))
            print(path_file)
            for file in file_names:
                if file.split('.')[-1] == 'srt':
                    print(path_file+'/'+file)
                    file = Triple_file_extension(file, path_file)
                    file.create_file()


if __name__ == "__main__":
    main()
