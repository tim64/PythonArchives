# -*- coding: utf-8 -*-
'''
import socket
print socket.gethostbyname('cn.ru')
print socket.gethostbyname_ex('cn.ru')
print socket.gethostbyaddr('195.189.238.85')
'''

# -*-coding: cp1251




def scaner_ports(hostname):
    import socket, urllib2
    HOST = hostname



    ports = [21, 22, 23, 25, 38, 43, 80, 109, 110, 115, 118, 119, 143,
    194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
    3306, 4000, 4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200]

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket object
        sock.settimeout(1) #Timeout
        try:
            sock.connect((HOST, port))
        except:
            print ("Port %s closed" % port)
            continue
        try:
            result = sock.recv(1024)
            print ("Received: %s port: %s" %port,result)
        except:
            print ("Port %s open." % port)
    sock.close()
    return 0

#scaner_ports('cn.ru')

def loginsite(hostname, login, passwd):
    import urllib2
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(realm='PDQ Application',
                          uri='http://'+ hostname,
                          user = login,
                          passwd = passwd)
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    urllib2.urlopen('http://vkontakte.ru')

loginsite('vkontakte.ru','tim32','vkontaktetim32')

