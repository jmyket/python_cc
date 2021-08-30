# EX 10-5: PROGRAMMING POLL

import os

os.chdir(f"{os.getcwd()}/chapter_10_files_exceptions")

file10_5 = "programming_poll.txt"

while True:
    poll = input("Why do you enjoy programming? (enter 'q' to quit): ")
    if poll == "q":
        break
    with open(file10_5, 'a') as file_obj:
        file_obj.write(f"{poll}\n")