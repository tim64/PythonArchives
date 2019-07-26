# -*- coding: utf-8 -*-


def process_list():
    import subprocess
    proc_list = subprocess.Popen('tasklist/fo "csv" /nh', shell=True, stdout=subprocess.PIPE).communicate()[0].split('\n')[1:]

    banlist = """","""
    clean = []
    for item in proc_list:
        for char in item:
            if banlist.find(char)>-1:
                item=item.replace(char,'')
        if (item.find('.exe')>-1):
            i=item.index('.exe')
            new_item = item[:i]+item[len(item):]
            clean.append(new_item)
    return clean



def analyse_process():
    list = process_list()
    for i in list:
        if i == 'AIMP3':
            print "Tim lisent musik!"
        if i == 'Photoshop':
            print 'Tim draw picture!'

count = 0
for i in range(1,22):
    if i%2 == 0:
        count = count + 1
        print i
        print count

