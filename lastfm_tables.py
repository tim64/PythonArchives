import os, re, word_collision

def clear_songlist(songlist):
    del_indexes = []
    i = 0
    for song in songlist:
        print song
        if song == []:
            del_indexes.append(i)
        i += 1
    print del_indexes


def get_artistpath():
    for root, dirs, files in os.walk('H:\Music'):
        for name in dirs:
            name = name.lower()
            print files

print get_artistpath()

