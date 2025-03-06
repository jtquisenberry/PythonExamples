import os
import glob
import random
import timeit


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

            with open(left_fq_filename, 'rb') as left_file, open(right_fq_filename, 'rb') as right_file:
                a = left_file.read()
                b = right_file.read()
                # print(a == b)
                # c = 1
                c = a == b

    def evaluate_file_matches2(self):
        for partial_filename in self.in_both:
            left_fq_filename = os.path.join(self.local_path, partial_filename)
            right_fq_filename = os.path.join(self.remote_path, partial_filename)
            left_file_size = os.path.getsize(left_fq_filename)
            right_file_size = os.path.getsize(right_fq_filename)
            if left_file_size != right_file_size:
                return False
            if not os.path.isfile(left_fq_filename):
                return True

            left_bytes = list()
            right_bytes = list()
            with open(left_fq_filename, 'rb') as left_file, open(right_fq_filename, 'rb') as right_file:
                for i in range(100):
                    position = random.randint(0, left_file_size)
                    left_file.seek(position)
                    left_byte = left_file.read(1)
                    left_bytes.append(left_byte)
                    right_file.seek(position)
                    right_byte = right_file.read(1)
                    right_bytes.append(right_byte)
                # print(left_bytes == right_bytes)
                xxx = left_bytes == right_bytes




fs = FileSyncer(local_path='D:\\Development\\temp\\',
                remote_path=r'D:\Development\temp2')

time_taken_function = timeit.timeit(fs.evaluate_path_matches, number=10000)
print(f"Time taken for function: {time_taken_function} seconds")

time_taken_function = timeit.timeit(fs.evaluate_file_matches2, number=10000)
print(f"Time taken for function: {time_taken_function} seconds")

# fs.evaluate_path_matches()
# fs.evaluate_file_matches2()



