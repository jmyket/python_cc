# 8-12: SANDWICHES

def make_sandwich(*fixins):
    print("Preparing your sandwich:")
    for fix in fixins:
        print(f"\t- {fix.title()}")

make_sandwich("6-inch", "italian", "toasted", "mayo", "honey mustard", "lettuce", "onion", "sweet peppers")
make_sandwich("foot-long", "meatball", "provolone cheese")
make_sandwich("6-inch", "ham", "american cheese", "mayo", "tomato")