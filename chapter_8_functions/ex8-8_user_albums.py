# 8-8: USER ALBUMS

while True:
    print("Please enter an Artist and Album.\nEnter 'q' to quit.")
    art = input("Artist Name: ")
    if art == 'q':
        break
    alb = input("Album Title: ")
    if alb == 'q':
        break
    make_album(artist = art, album = alb)