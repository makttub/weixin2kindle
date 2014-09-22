#coding: utf-8

import sys,urllib2
from HTMLParser import HTMLParser
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from lxml import etree

class getArticleError(StandardError):
    pass

class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()


class pubAccount(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        # self.getTitleUrl(url)

    def getTitleUrl(self):
        r = Render(self.url)
        htmlCont = r.frame.toHtml()
        src = unicode(htmlCont)
        tree = etree.HTML(src)

        urls = tree.xpath(u"//*[@id=\"sogou_vr_11002601_title_0\"]/@href")
        titles = tree.xpath(u"//*[@id=\"sogou_vr_11002601_title_0\"]/text()")

        if len(urls) != len(titles):
            raise getArticleError()

        self.titleUrl = dict(zip(titles,urls))

        # for i in range(len(self.urls)):
        #     self.send = True

        return self.titleUrl

if __name__ == '__main__':
    url = u'http://weixin.sogou.com/gzh?openid=oIWsFt1FSztdLmdVbgYcZFJ8p9Fg'
    mintshow = pubAccount('mintshow', url)
    mintshow.getTitleUrl(mintshow.url)
    # url = 'http://weixin.sogou.com/gzh?openid=oIWsFt98u7kmyb9-OpSPghHa7Uiw'
    # sagacitymac = pubAccount('sagacitymac', url)
    # sagacitymac.getTitleUrl(sagacitymac.url)
    print mintshow.titleUrl
