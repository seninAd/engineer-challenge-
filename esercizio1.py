import os
import sys

def string_in_file(filename, old_string, new_string):
    with open(filename, 'r') as file:
        file_data = file.read()

    file_data = file_data.replace(old_string, new_string)

    with open(filename, 'w') as file:
        file.write(file_data)

def string_in_directory(directory, old_string, new_string):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            string_in_file(filepath, old_string, new_string)

if __name__ == '__main__':
    old_string = sys.argv[1]
    new_string = sys.argv[2]
    directory = sys.argv[3]

    string_in_directory(directory, old_string, new_string)
