#coding=utf-8

import sys, os, re
from ID3 import *
text = open('tim32love.txt','r')


def parser(text):
    title_list = []
    creator_list = []
    lines = text.readlines()
    for line in lines:
        start_count_title = line.count('<title>')
        end_count_title  = line.count('</title>')
        start_count_creator = line.count('<creator>')
        end_count_creator  = line.count('</creator>')

        if (start_count_title <>0) and (end_count_title  <> 0):
            start_title = line.index('<title>')+len('<title>')
            end_title = line.index('</title>')
            subline_title=line[start_title:end_title]
            title_list.append(subline_title)

        if (start_count_creator <>0) and (end_count_creator  <> 0):
            start_creator = line.index('<creator>')+len('<creator>')
            end_creator  = line.index('</creator>')
            subline_creator=line[start_creator:end_creator]
            creator_list.append(subline_creator)
    return title_list,creator_list



def findfiles(title,artist):
    for root, dirs, files in os.walk(ur'H:\Music\Mantus'):
        for f in files:
            if '.mp3' in f:
                path = (os.path.join(root,f))
                song = ID3(path)
                if (song.title == title) and (song.artist == artist):
                    return path



def form_paths():
    paths = ''
    titles, artists = parser(text)
    for i in range(len(titles)):
        names = findfiles(titles[i],artists[i])
        if names <> None:
            paths += findfiles(titles[i],artists[i]) + '\n'
    return paths

print form_paths()