# -*- coding: utf-8 -*-
# http://www.yegorov-p.ru/opisanie-formata-jtv
import codecs,datetime
from filetimes import filetime_to_dt, dt_to_filetime

#Перобразовывает байты в целое. Если второй байт = 0, он не учитывается
#! - Переделать под кол-во записей больше чем 255
def bytearray_to_count(byte_array):
    my_hex = ''
    for item in byte_array:
        if item <> '0x0':
            if len(item) <= 3:
                tmp = str(item).replace('0x','0')
            else:
                tmp = str(item).replace('0x','')
            my_hex += tmp
    return int('0x'+ my_hex,16)

#Функция возвращает число из группы байт (в hex)
def bytearray_to_dec_reverced(byte_array):
    my_hex = ''
    for item in reversed(byte_array):
        if len(item) <= 3:
            tmp = str(item).replace('0x','0')
        else:
            tmp = str(item).replace('0x','')
        my_hex += tmp
    return int('0x'+ my_hex,16)

def get_time(filetime):
    return filetime_to_dt(filetime)

#Функция get_times
#Сохраняем время. Первые два байта - кол-во записей. Их не учитываем.
#Один блок 12 байт. Первые 2 байта - нулевые. След. 8 - время (filetime).
#След 2 - смещение в pdt файле
def get_times(filename):
    tmp = []
    times = []
    begin = 2
    f = codecs.open(filename, 'rb')
    data = f.read()
    for i in range(2,len(data)):
        if (i%12) == 0:
            end = i + 2
            for i in data[begin:end]:
                tmp.append(hex(ord(i)))
            begin = end
            times.append(tmp[2:-2]) #Записываем время. Отбрасываем первые и последние два байта
            tmp = []
    return times
#Функция get_offsets
#Сохраняем смезения. Последние два байта в 12 байтовом блоке.
def get_offsets(filename):
    tmp = []
    offsets = []
    begin = 2
    f = codecs.open(filename, 'rb')
    data = f.read()
    for i in range(2,len(data)):
        if (i%12) == 0:
            end = i + 2
            for i in data[begin:end]:
                tmp.append(hex(ord(i)))
            begin = end
            offsets.append(tmp[-2:]) #Записываем смещение
            tmp = []
    return offsets
#Переводим байты смещения в десятичный вид
def dec_offsets(offsets):
    dec_array = []
    for item in offsets:
        dec_array.append(bytearray_to_dec_reverced(item))
    return dec_array

#Функция, которая выдает дату и время в нормальном формате
def get_time_list(times):
    normal_times =[]
    for item in times:
        timestamp = bytearray_to_dec_reverced(item)
        normal_times.append(get_time(timestamp))
    return normal_times