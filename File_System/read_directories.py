import sys
import os
import random


class FileHandler:

    def __init__(self, in_directory):

        self.in_directory = in_directory
        self.file_dictionary = dict()


    def print_current_directories(self):
        print(os.getcwd())
        print(os.getcwdu())



    def print_files(self):

        for root, subdirs, files in  os.walk(self.in_directory):
            # print(root)
            for f in files:
                print(root, f)


    def make_file_dictionary(self):

        for root, subdirs, files in os.walk(self.in_directory):
            for f in files:
                file_without_extension = os.path.splitext(f)[0]

                if file_without_extension not in self.file_dictionary:
                    self.file_dictionary[file_without_extension] = root


if __name__ == '__main__':
    fh= FileHandler(r'E:\W\emu\CDi')
    fh.make_file_dictionary()

    if len(fh.file_dictionary) > 0:
        file_number = random.randint(0,len(fh.file_dictionary))

        sample_file = list(fh.file_dictionary.keys())[file_number]
        print(sample_file, fh.file_dictionary[sample_file])
    a = 1