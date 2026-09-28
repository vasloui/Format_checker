import sys
import os 

def list_dir_files(home):
    for name in os.listdir(home):
        path = os.path.join(home, name)
        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            print(path)
            list_dir_files(path)


def check_greek(home):
    # Greek Letters are not allowed
    # Greek utf-8 letters range
    # https://www.charset.org/utf-8
    greek = (880, 993)

    for name in os.listdir(home):
        path = os.path.join(home, name)
        if os.path.isfile(path):
            for i in name:
                if ord(i) <= greek[1] and ord(i) >= greek[0]:
                    print(path)
                    break

        elif os.path.isdir(path):
            for i in name:
                if ord(i) <= greek[1] and ord(i) >= greek[0]:
                    print(path)
                    break
            check_greek(path)


if sys.argv[1] == "print_parameters":
    print(sys.argv)

if sys.argv[1] == "list_dir_files":
    list_dir_files(sys.argv[2])


if sys.argv[1] == "help":
    print("""
    Options:
    print_parameters: lists command line parameters
    list_dir_files [dir]: Lists recursively all directories and files
    help: Shows help
    tar_gz_win [dir]: Format checks the specified directory for directories and files
                        that are illegal for gz-taring a directory on windows and outputs the 
                        paths.  
    
    """)

if sys.argv[1] == "check_greek":
    check_greek(sys.argv[2])