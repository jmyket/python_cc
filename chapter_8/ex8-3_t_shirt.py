# 8-3: T-SHIRT

def make_shirt(size, text):
    """Display shirt info."""
    if len(size) == 2:  
        print(
            f"Shirt order: size = {size.upper()}; message = {text}."
        )
    else:
        print(
            f"Shirt order: size = {size.title()}; message = {text}."
        )

make_shirt("XL", "I like pizza!") # POSITIONAL CALL
make_shirt(size = "X-large", text = "I like pizza!") # ARGUMENT CALL