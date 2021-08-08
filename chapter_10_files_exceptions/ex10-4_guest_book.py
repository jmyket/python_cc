# EX 10-4: GUEST BOOK

import os

os.chdir(f"{os.getcwd()}/chapter_10_files_exceptions")

file10_4 = "guest_book.txt"

while True:
    u_name = input("Please enter your name (or enter 'q' to quit): ")
    if u_name == "q":
        break
    print(f"Hi {u_name}, thanks for coming!")
    with open(file10_4, 'a') as file_obj:
        file_obj.write(f"{u_name}\n")