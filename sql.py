#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import re,random


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url  not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()

'''
a = UrlManager()
print a
a.add_new_url('www.baidu.com')
a.add_new_url('www.google.com')
u = ('www.caoliu.com','www.taobao.com')
a.add_new_urls(u)
#a.add_new_urls('www.caoli.com','www.1024.com')
#a.add_new_urls('www.google.com')
print a.has_new_url()
#print a.get_new_url()
print a.new_urls
print a.old_urls
'''

class Downloader(object):
    def get(self,url):
        r = requests.get(url,timeout = 10)
        if r.status_code != 200:
            return None
        _str = r.text
        return _str

    def post(self,url,data):
        r = requests.post(url,data)
        _str = r.text
        return _str

    def download(self,url,htmls):
        if url is None:
            return None
        _str = {}
        _str["url"] = url
        try:
            r = requests.get(url,timeout = 10)
            if r.status_code != 200:
                return None
            _str["html"] = r.text
        except Exception as e:
            return None
        htmls.append(_str)

'''
h = []
d = Downloader()
t = d.get('http://www.baidu.com')
t1 = d.post('http://www.baidu.com','123456')
t2 = d.get('http://t66y.cn')
t3 = d.download('http://www.baidu.com',h)
print t
print '============================================'
print t1
print '============================================'
print "t2 =" +  t2
print '============================================'
print t3
print '============================================'
print h
'''
