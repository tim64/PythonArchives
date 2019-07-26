# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import os, id3reader, urllib2, word_collision

lastfm_key="acb7e0b5d3b7084c491d8720340e43d5"
lastfm_user="tim32"
lastfm_url ="http://ws.audioscrobbler.com/2.0/"
limit = "100"




#http://ws.audioscrobbler.com/2.0/?method=user.getlovedtracks&user=USER&api_key=API_KEY
def CreateRequest(user):
    request = lastfm_url + "?method=user.getlovedtracks&user="+user+"&api_key="+lastfm_key+"&limit="+limit
    return request

def GetList(user):
    url = CreateRequest(user)
    print "Url found \n" + url
    resp=urllib2.urlopen(url)
    page=resp.read()
    return page


def GetTagList(user):
    i = 1
    doc = open("lovelist.txt", "w+")
    doc.write(GetList(user))    #Скачиваем список текст в файл
    doc.close()
    doc = open(r'lovelist.txt')
    xml = doc.read()
    doc.close()
    artist = []
    title = []
    bool = 0

    #Парсим XML
    soup = BeautifulSoup(''.join(xml))
    #print soup.prettify()
    #tag = soup.lfm.lovedtracks.track.artist.name
    names = soup.findAll(u'name')

    for item in names:
        tmp = unicode(item)
        tmp = tmp.replace('<name>','')
        tmp = tmp.replace('</name>','')
        if i%2 != 0:
            title.append(tmp)
        else:
            artist.append(tmp)
        i += 1
    return artist,title

def simplification(wordlist):
    new = []
    for word in wordlist:
        newword = word_collision.simpler(word)
        new.append(newword)
    return new

def titleCmp(song1, song2):
    tmp1 = song1.lower()
    tmp2 =song2.lower()
    if tmp1 == tmp2:
        return 1
    else:
        return 0

def GetArtistPath(top, name):
    for root, dirs, files in os.walk('H:\Music'):
        if name in dirs:
            return os.path.join(root,name)

def findfiles(artist, title):
    folder = u'H:\Music\\'+artist
    print folder
    for root, dirs, files in os.walk(folder):
        for f in files:
            if '.mp3' in f:
                path = os.path.join(root,f)
                #print path
                try:
                    tag = id3reader.Reader(unicode(path))
                except ValueError:
                    return None

                if tag != None:
                    mp3title = tag.getValue('title')
                    mp3artist = tag.getValue('performer')
                    if (mp3artist != None) and (mp3title != None):
                        if (titleCmp(tag.getValue('title'), title) == 1) and (titleCmp(tag.getValue('performer'), artist) == 1):
                            print "File found! - ",path
                            return path

def main():
    path = []
    count = 0
    doc = open("mylist.m3u", "w")
    artist,title = GetTagList("tim32")

    for i in range(len(title)):
        #print "Scan [",artist[i],' - ',title[i],']'
        tmp = findfiles(artist_normalname[i],artist[i],title[i])
        if tmp != None:
            path.append(tmp)
            print tmp
    for i in path:
        doc.write(i.encode('utf-8')+'\n')
    print len(title)," to ",len (path)

    doc.close()


main()





















