# -*- coding: utf-8 -*-
import NDX_Reader, PDT_Reader, time, datetime, sys, os
from zipfile import ZipFile
# Первый аргумент - архив. Второй аргумент = Название канала.
filename = sys.argv[1]
channel = sys.argv[2]
#Константы
path = os.getcwd()               #Путь к скрипту
ndx_name = channel + ".ndx"      #Имя NDX файла
ndx_path = path+'\\'+ndx_name    #Путь к извлеченному NDX файлу
pdt_name = channel + ".pdt"      #Имя PDT файла
pdt_path = path+'\\'+pdt_name    #Путь к извлеченному PDT файлу
dt_utc = datetime.datetime.utcnow()# Текущее время с учетом часового пояса
dt_utc_second = time.mktime(dt_utc.timetuple())# Количество секунд (для UTC)

#Главная функция
def main(filename, channel):
    #Работа с архивом
    #!- Файлы с русской кодировкой не извлекает
    jtv = ZipFile(filename, 'r')
    jtv.extract(ndx_name,path)
    jtv.extract(pdt_name,path)
    #--- Работа с NDX ---
    #Сохраняем время
    time_bytes = NDX_Reader.get_times(ndx_path)
    normal_times = NDX_Reader.get_time_list(time_bytes)
    #Запоминае смещение
    offsets = NDX_Reader.get_offsets(ndx_path)
    offsets = NDX_Reader.dec_offsets(offsets)
    count = len(offsets)
    #--- Работа с PDT ---
    #Получаем список программ
    programs = PDT_Reader.pdt_parser(pdt_path,offsets)
    for i in range(count):
        print "Time: " + str(normal_times[i]) + " Title: " + programs[i]
    #Удаляем извлеченные файлы
    print ndx_path
    os.remove(ndx_path)
    os.remove(pdt_path)

main(filename,channel)