# EX 10-6: ADDITION

def add_nums():
    print("Provide two numbers and they will be added together.")

    num_1 = input("What is the first number? ")
    num_2 = input("What is the second number? ")

    try:
        s = int(num_1) + int(num_2)
    except ValueError:
        print(
            "Unable to add your entries. Please make sure both are valid
            "numbers."
        )
    else:
        print(f"{num_1} + {num_2} = {s}")

add_nums()