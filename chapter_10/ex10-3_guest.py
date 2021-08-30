# EX 10-3: GUEST

import os

os.chdir(f"{os.getcwd()}/chapter_10_files_exceptions")

u_name = input("Please enter your name: ")

file10_3 = "guest.txt"
with open(file10_3, 'w') as file_obj:
    file_obj.write(u_name)