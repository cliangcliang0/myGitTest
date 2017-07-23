#! /usr/bin/env python
#-*- coding:utf-8 -*-

import urllib2

def clear():
    time.sleep(3)
    OS = platform.system()
    if (OS == u'windows'):
        OS.system('cls')
    else:
        OS.system('clear')

def linkBaidu():
    url = 'http://www.baidu.com'
    try:
        response = urllib2.urlopen(url,timeout =3)
    except urllib2.URLError:
        print("Netaddress Error!")
    with open('./baidu.txt','w') as fp:
        fp.write(response.read())
    print(response.geturl())
    print(response.getcode())
    print(response.info())

if __name__ == '__main__':
    linkBaidu()
