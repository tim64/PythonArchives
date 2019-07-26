from string import ascii_lowercase as alpha
import string

indexes = range(25)
print indexes
set = [8.1, 1.4, 2.7, 3.9, 13.0, 2.9, 2.0, 5.2, 6.5, 0.2, 0.4, 3.4, 2.5, 7.2, 7.9, 2.0, 1.55, 6.9, 6.1, 10.5, 2.4, 0.9, 1.5, 0.2, 1.9, 0.1]


def oneletter(text, letter):
    return text.count(letter)

def friq(text):
    f_text = []
    from MyString import trash
    text=trash(text)
    text=text.lower()
    size = len(text)
    from string import ascii_lowercase as alpha
    for let in alpha:
        f_text.append(((oneletter(text,let)*1.0)/size)*100)
    return f_text


def form(set):
    from MyString import strTOlist,listTOstr
    al = alpha
    tmp = []
    res = []
    tmp = strTOlist(al)
    while(1):
        if max(set) == -1:
            return listTOstr(res)
        max_item_pos = set.index(max(set)) #Max position
        res.append(al[max_item_pos ]) #Add new max element
        set[max_item_pos]=-1 #Kill element


text = open('ord.txt','r').read()
#etalon = form(set)
friqs = form(friq(text))
print alpha
print friqs

#table = string.maketrans(alpha, friqs)
#text = text.translate(table)
#print text