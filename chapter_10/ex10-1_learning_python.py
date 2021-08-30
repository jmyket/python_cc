# EX 10-1: LEARNING PYTHON
import os

os.chdir(f"{os.getcwd()}/chapter_10_files_exceptions")
filename = "learning_python.txt"

with open(filename) as lp_file:
    for line in lp_file:
        print(line)   

with open(filename) as lp_file:
    full_file = lp_file.read()

print(full_file)

with open(filename) as lp_file:
    file_lines = lp_file.readlines()

for line in file_lines:
    print(line.strip())