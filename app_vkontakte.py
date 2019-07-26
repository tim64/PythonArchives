import httplib, urllib
import sys
import re

def main():
    browser = httplib.HTTPConnection("vkontakte.ru")
    browser.request("GET", "/") # get main page
    response = browser.getresponse()
    if response.status != 200:  # error checking
        print "Something went wrong"
        sys.exit(1)
    page = response.read()
    var_ip_h = re.search("ip_h: '(\d|\w*)'", page).group(1) # getting required vars
    var_hash = re.search("hash: '(\d|\w*)'", page).group(1)
    var_email = "fobos666@mail.ru"                           # your mail
    var_pass = "vkontaktetim32"                                      # your pass
    params = urllib.urlencode((('act', 'login'),
                               ('q', 1),
                               ('al_frame', 1),
                               ('expire', ''),
                               ('captcha_sid', ''),
                               ('captcha_key', ''),
                               ('from_host', 'vkontakte.ru'),
                               ('ip_h',  var_ip_h),
                               ('email', var_email),
                               ('pass',  var_pass)
                              ))
    headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1)",
               "Content-type": "application/x-www-form-urlencoded"
               }
    browser.close()
    browser = httplib.HTTPConnection("login.vk.com") # login request N1
    browser.request("POST",
                    "/?act=login",
                    params,
                    headers)
    response = browser.getresponse()
    location = re.search("vkontakte.ru(.*)", response.getheader('Location')).group(1)
    browser.close()
    browser = httplib.HTTPConnection("vkontakte.ru") # login request N2
    browser.request("POST",
                    location,
                    params,
                    headers)
    response = browser.getresponse()
    cookies = re.search("(remixsid=.*;) expires", response.getheader('set-cookie')).group(1) # getting cookies
    location = response.getheader('Location') # user id
    headers = {"Cookie" : cookies}
    browser.request("GET", location, '', headers) # now you can anywhere you want
    response = browser.getresponse()
    data = response.read()
    output = open('out.html', 'w')
    output.write(data)



#!!!!!! main is called here:
main()
