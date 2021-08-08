# 8-7: ALBUM

def make_album(artist, album, tracks = None):
    """Album dictionary."""
    if tracks:
        albums = {'artist' : artist.title(), 'album' : album.title(), 'tracks' : tracks}
    else:
        albums = {'artist' : artist.title(), 'album' : album.title()}
    return albums

make_album(artist = "Talking heads", album = "fear of music")
make_album(artist = "tool", album = "10,000 days")
make_album(artist = "cannibal corpse", album = "the bleeding")

make_album(artist = "cannibal corpse", album = "the bleeding", tracks = 11)