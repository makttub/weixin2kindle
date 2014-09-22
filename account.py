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

    def getTitleUrl(self, url):
        r = Render(url)
        htmlCont = r.frame.toHtml()
        src = unicode(htmlCont)
        tree = etree.HTML(src)

        self.urls = tree.xpath(u"//*[@id=\"sogou_vr_11002601_title_0\"]/@href")
        self.titles = tree.xpath(u"//*[@id=\"sogou_vr_11002601_title_0\"]/text()")

        if len(self.urls) != len(self.titles):
            raise getArticleError()

        # for i in range(len(self.urls)):
        #     self.send = True

        return self.urls, self.titles

if __name__ == '__main__':
    # url = u'http://weixin.sogou.com/gzh?openid=oIWsFt1FSztdLmdVbgYcZFJ8p9Fg'
    # mintshow = pubAccount('mintshow', url)
    url = 'http://weixin.sogou.com/gzh?openid=oIWsFt98u7kmyb9-OpSPghHa7Uiw'
    sagacitymac = pubAccount('sagacitymac', url)
    sagacitymac.getTitleUrl(sagacitymac.url)
    print sagacitymac.titles
    print sagacitymac.urls
