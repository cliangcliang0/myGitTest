#!/usr/bin/env python
#-*- coding:utf-8 -*-

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
