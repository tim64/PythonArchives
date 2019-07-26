# -*- coding: utf-8 -*-
import codecs,string,datetime,os
from filetimes import filetime_to_dt, dt_to_filetime

#Главная функция. Возвращает список программ
def pdt_parser(filename,offsets):
    f = codecs.open(filename, 'rb',"cp1251")
    data = f.read()
    program_list = get_program_list(data,offsets)
    return program_list

#Функция, которая формерует список программ по заданному списку смещений.
def get_program_list(data, offsets):
    programs = []
    for item in offsets:
        programs.append(get_program(data,item))
    return programs

#Чтение файла телепрограмм. Начало чтения - offset.
#Размер записи - значение в байте c смещением offset
def get_program(data, offset):
    begin = offset
    length = ord(data[begin])
    for i in range(begin,len(data)):
        return data[begin+2:begin+2+length]
















