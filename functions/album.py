def make_album(artist, name_of_album, musics=None):
    album = {"artist": artist.title(), "album": name_of_album.title()}
    if musics:
        album["number of musics:"] = musics
    return album

link_park = make_album("link park", "meteora")
print(link_park)
missinho = make_album("missinho", "anjos do forro")
print(missinho)
a7x = make_album("avenged sevenfold", "nightmare", 20)
print(a7x)

while True:
    print("Are we going to put together the album of your favorite band?")
    print("When you want to leave press 'q' at any time.")

    artist = input("Artist: ")
    if artist == "q":
        break
    album_name = input("Name of album: ")
    if album_name == "q":
        break

    album_dicionary = make_album(artist, album_name)
    print(album_dicionary)
