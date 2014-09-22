#coding: utf-8

import sys,urllib
from lxml import etree
import re

class getArticleError(StandardError):
    pass

class pubAccount(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.getTitleUrl()

    def getTitleUrl(self):
        xmlurl = 'http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&' + self.url[28:] + '&page=1'
        xml = urllib.urlopen(xmlurl).read()
        retitle = re.compile(r'<title>.*?>')
        reurl = re.compile(r'<url>.*?>')

        retitles = retitle.findall(xml)
        reurls = reurl.findall(xml)

        if len(reurls) != len(retitles):
            raise getArticleError()

        titles=[]
        urls=[]

        for i in range(len(retitles)):
            titles.append(retitles[i][16:-3])
            urls.append(reurls[i][14:-3])

        self.titleUrl = dict(zip(titles,urls))
        return self.titleUrl

if __name__ == '__main__':
    mintshow = pubAccount('mintshow', u'http://weixin.sogou.com/gzh?openid=oIWsFt1FSztdLmdVbgYcZFJ8p9Fg')
    sagacitymac = pubAccount('sagacitymac', u'http://weixin.sogou.com/gzh?openid=oIWsFt98u7kmyb9-OpSPghHa7Uiw')
    print mintshow.titleUrl
    print sagacitymac.titleUrl
