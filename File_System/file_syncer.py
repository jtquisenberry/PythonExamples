import os
import glob
import random

class FileSyncer:
    def __init__(self, local_path='', remote_path=''):
        self.local_path = local_path
        self.remote_path = remote_path
        self.left_only = set()
        self.right_only = set()
        self.in_both = set()

    def find_matches(self):
        pass

    def get_files2(self, folder):
        files = []
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                files.append(file)
        return files

    def get_files3(self, folder):
        files = []
        for root, dirs, files in os.walk(folder):
            print(root, dirs)
            for file in files:
                print(root, dirs, file)
                #    files.append(file)
        return files

    def get_files(self, directory, pattern='**'):
        """
        Recursively finds files matching the given pattern and processes them.

        :param directory: The root directory from which to start the search.
        :param pattern: The pattern to match, e.g. "*.txt", "**/*.py").
        :return: A list of paths ignoring the portion of the path matching `directory`.
        """

        directory = os.path.normpath(directory)
        mid_position = len(directory) + 1
        partial_files = set()
        partial_directories = set()
        for fq_filename in glob.glob(os.path.join(directory, pattern), recursive=True):
            partial_filename = fq_filename[mid_position:]
            if partial_filename:
                partial_files.add(partial_filename)
        return partial_files, partial_directories

    def evaluate_path_matches(self):
        left_files, left_directories = self.get_files(self.local_path)
        right_files, right_directories = self.get_files(self.remote_path)
        self.left_only = left_files.difference(right_files)
        self.right_only = right_files.difference(left_files)
        self.in_both = left_files.intersection(right_files)

    def evaluate_file_matches(self):
        for partial_filename in self.in_both:
            left_fq_filename = os.path.join(self.local_path, partial_filename)
            right_fq_filename = os.path.join(self.remote_path, partial_filename)
            left_file_size = os.path.getsize(left_fq_filename)
            right_file_size = os.path.getsize(right_fq_filename)
            if left_file_size != right_file_size:
                return False


            for i in range(left_file_size):



            with open(left_fq_filename, 'rb') as left_file:
                pass

            with open(right_fq_filename, 'rb') as right_file:
                pass





fs = FileSyncer(local_path='D:\\Development\\temp\\',
                remote_path=r'D:\Development\temp2')

fs.evaluate_path_matches()

x = fs.get_files2(fs.local_path)

z = 1


    # Obține lista de fișiere pentru fiecare folder
    # files_folder1 = get_files(folder1)
    # files_folder2 = get_files(folder2)
