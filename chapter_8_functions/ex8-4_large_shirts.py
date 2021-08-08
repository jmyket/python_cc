# 8-4: LARGE SHIRTS

def make_shirt_2(size = "L", text = "I love Python!"):
    """Display shirt info."""
    if len(size) == 2:  
        print(
            f"Shirt order: size = {size.upper()}; message = {text}."
        )
    else:
        print(
            f"Shirt order: size = {size.title()}; message = {text}."
        )

make_shirt_2() # LARGE SHIRT W/ DEFAULT MESSAGE
make_shirt_2(size = "m") # MEDIUM SHIRT W/ DEFAULT MESSAGE
make_shirt_2(size = "xl/t", text = "Tall Sizes!!!!")