#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
import re,random
import threading
from urlparse import urljoin
from bs4 import BeautifulSoup
import sys



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

class SpiderMain(object):
    def __init__(self,root,threadNum):
        self.urls = UrlManager()
        self.download = Downloader()
        self.root = root
        self.threadNum = threadNum

    def _judge(self,domain,url):
        if(url.find(domain) != -1):
            return True
        else:
            return False

    def _parse(self,page_url,content):
        if content is None:
            return
        soup = BeautifulSoup(content,'html.parser')
        _news = self._get_new_urls(page_url,soup)
        return _news

    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a')
        for link in links:
            new_url = link.get('href')
            new_full_url = urljoin(page_url,new_url)
            if(self._judge(self.root,new_full_url)):
                new_urls.add(new_full_url)
        return new_urls

    def craw(self):
        self.urls.add_new_url(self.root)
        while self.urls.has_new_url():
            _content = []
            th = []
            for i in list(range(self.threadNum)):
                if self.urls.has_new_url() is False:
                    break
                new_url = self.urls.get_new_url()
                
                ##sql check

                print "craw:"
                print new_url
                t = threading.Thread(target = self.download.download,args=(new_url,_content))
                t.start()
                th.append(t)

            for t in th:
                t.join()
            for _str in _content:
                if _str is None:
                    continue
                new_urls = self._parse(new_url,_str["html"])
                self.urls.add_new_urls(new_urls)


def main():
    root = "http://www.shiyanlou.com/"
    threadNum = 10
    #spider
    w8  = SpiderMain(root,threadNum)
    w8.craw()

if __name__ == '__main__':
    main()




