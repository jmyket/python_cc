# EX 10-2: LEARNING C

import os

os.chdir(f"{os.getcwd()}/chapter_10_files_exceptions")
filename = "learning_python.txt"

with open(filename) as lp_file:
    full_file = lp_file.read()

print(full_file.replace("Python", "R"))

