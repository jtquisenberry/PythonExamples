import os
import glob
import random
import hashlib
import filecmp
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

    def get_files(self, directory, pattern='**'):  # noqa Method is static
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

    def in_left_only(self):
        return self.left_only

    def in_right_only(self):
        return self.right_only

    def in_left_and_right(self):
        return self.in_both

    def delete_left(self):
        pass

    def delete_left_only(self):
        files = list()
        for partial_file in self.left_only:
            file = os.path.join(self.local_path, partial_file)
            files.append(file)
        self.delete_contents(files)

    def delete_right(self):
        pass

    def delete_right_only(self):
        files = list()
        for partial_file in self.right_only:
            file = os.path.join(self.remote_path, partial_file)
            files.append(file)
        self.delete_contents(files)

    def delete_contents(self, files):  # noqa Method is static
        for file in files:
            os.remove(file)

    def delete_all(self, files, directories):  # noqa Method is static
        for file in files:
            os.remove(file)
        for directory in directories:
            os.rmdir(directory)

    def copy_files(self):
        pass

    def evaluate_file_matches_full(self):
        for partial_filename in self.in_both:
            left_fq_filename = os.path.join(self.local_path, partial_filename)
            right_fq_filename = os.path.join(self.remote_path, partial_filename)
            left_file_size = os.path.getsize(left_fq_filename)
            right_file_size = os.path.getsize(right_fq_filename)
            if left_file_size != right_file_size:
                return False
            if not os.path.isfile(left_fq_filename):
                return True

            with open(left_fq_filename, 'rb') as left_file, open(right_fq_filename, 'rb') as right_file:
                a = left_file.read()
                b = right_file.read()
                # print(a == b)
                c = a == b

    def evaluate_file_matches_random_100(self):
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
                c = left_bytes == right_bytes

    def evaluate_file_matches_random_100_sorted(self):
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
                positions = list()
                for i in range(100):
                    position = random.randint(0, left_file_size)
                    positions.append(position)
                positions.sort()
                for position in positions:
                    left_file.seek(position)
                    left_byte = left_file.read(1)
                    left_bytes.append(left_byte)
                    right_file.seek(position)
                    right_byte = right_file.read(1)
                    right_bytes.append(right_byte)
                c = left_bytes == right_bytes

    def evaluate_file_matches_filecmp(self):
        for partial_filename in self.in_both:
            left_fq_filename = os.path.join(self.local_path, partial_filename)
            right_fq_filename = os.path.join(self.remote_path, partial_filename)
            left_file_size = os.path.getsize(left_fq_filename)
            right_file_size = os.path.getsize(right_fq_filename)
            if left_file_size != right_file_size:
                return False
            if not os.path.isfile(left_fq_filename):
                return True

            c = filecmp.cmp(left_fq_filename, right_fq_filename, shallow=False)


    def evaluate_file_matches_md5(self):
        for partial_filename in self.in_both:
            left_fq_filename = os.path.join(self.local_path, partial_filename)
            right_fq_filename = os.path.join(self.remote_path, partial_filename)
            left_file_size = os.path.getsize(left_fq_filename)
            right_file_size = os.path.getsize(right_fq_filename)
            if left_file_size != right_file_size:
                return False
            if not os.path.isfile(left_fq_filename):
                return True

            with open(left_fq_filename, 'rb') as left_file, open(right_fq_filename, 'rb') as right_file:
                left_binary = left_file.read()
                right_binary = right_file.read()
                left_md5 = hashlib.md5(left_binary).hexdigest()
                right_md5 = hashlib.md5(right_binary).hexdigest()
                c = left_md5 == right_md5


fs = FileSyncer(local_path='D:\\Development\\temp\\',
                remote_path=r'D:\Development\temp2')

fs.evaluate_path_matches()

# time_taken_function = timeit.timeit(fs.evaluate_file_matches_full, number=10000)
# print(f"Time taken for function: {time_taken_function} seconds")
#
# time_taken_function = timeit.timeit(fs.evaluate_file_matches_random_100, number=10000)
# print(f"Time taken for function: {time_taken_function} seconds")
#
# time_taken_function = timeit.timeit(fs.evaluate_file_matches_random_100_sorted, number=10000)
# print(f"Time taken for function: {time_taken_function} seconds")
#
# time_taken_function = timeit.timeit(fs.evaluate_file_matches_filecmp, number=10000)
# print(f"Time taken for function: {time_taken_function} seconds")
#
# time_taken_function = timeit.timeit(fs.evaluate_file_matches_md5, number=10000)
# print(f"Time taken for function: {time_taken_function} seconds")

# fs.evaluate_path_matches()
# fs.evaluate_file_matches2()



