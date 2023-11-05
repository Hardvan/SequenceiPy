"""This module creates a directory with a given number of files with the following naming convention:
1_file.txt
2_file.txt
...
It first deletes the directory if it already exists.
Then it creates the directory and the files for testing the functionality
of the rename_files_with_padding function in SequenciPy.py.
"""

import os


def create_test_directory(directory_path, num_files):
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)

    for i in range(1, num_files + 1):
        file_name = f"{i}_file.txt"
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, 'w') as file:
            file.write(f"This is file {i}.\n")


def delete_test_directory(directory_path):
    if os.path.exists(directory_path):
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
        os.rmdir(directory_path)
        print(f"🗑️  Deleted {directory_path}")


if __name__ == "__main__":
    directory_path = "Directory1"
    num_files = 11

    delete_test_directory(directory_path)
    create_test_directory(directory_path, num_files)
    print(f"✅ Created {num_files} files in {directory_path}")
