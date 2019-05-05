import glob, os

def find_file(in_directory):

    pattern = in_directory + '\\' + '*.txt'


    for f in glob.glob(pattern, recursive=True):
        print(f)

if __name__ == '__main__':
    find_file(r'E:\w\emu\cdi')
    a = 1


