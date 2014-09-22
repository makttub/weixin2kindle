#coding: utf-8

import os
import sqlite3
import time
import account

class user(object):
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts
        abspath = os.path.abspath('.')
        self.dirpath = os.path.join(abspath, self.name)
        self.mkDir()
        self.mkTable()

    def mkDir(self):
        if not os.path.exists(self.dirpath):
            os.mkdir(self.dirpath)

    def checkList(self):
        dbdir = os.path.join(self.dirpath, 'sended.db')
        try:
            conn = sqlite3.connect(dbdir)
            cursor = conn.cursor()

            for i in range(len(self.accounts)):
                dellist = []
                for j in range(len(self.accounts[i].urls)):
                    cursor.execute('select * from send where url=?', (self.accounts[i].urls[j],))
                    result = cursor.fetchall()
                    if len(result) != 0:
                        dellist.append(i)
                    else:
                        cursor.execute("insert into send values ('%s','%s','%s')" % (self.accounts[i].name, self.accounts[i].titles[j], self.accounts[i].urls[j]))
                for k in dellist:
                    self.accounts[i].titles.pop(k)
                    self.accounts[i].urls.pop(k)
        finally:
            cursor.close()
            conn.commit()
            conn.close()


    def mkTable(self):
        try:
            dbdir = os.path.join(self.dirpath, 'sended.db')
            conn = sqlite3.connect(dbdir)
            cursor = conn.cursor()
            cursor.execute('create table if not exists send (account varchar(20), title not null, url not null)')
        finally:
            cursor.close()
            conn.commit()
            conn.close()

if __name__ == '__main__':
    # mintshow = account.pubAccount('mintshow', u'http://weixin.sogou.com/gzh?openid=oIWsFt1FSztdLmdVbgYcZFJ8p9Fg')
    sagacitymac = account.pubAccount('sagacitymac', u'http://weixin.sogou.com/gzh?openid=oIWsFt98u7kmyb9-OpSPghHa7Uiw')
    sagacitymac.titles = [u'\u4ece\u4ea7\u4e1a\u94fe\u5165\u624b, 360\u8054\u5408\u94f6\u8054\u5171\u540c\u6253\u9020\u79fb\u52a8\u652f\u4ed8\u5b89\u5168', u'\u8ba4\u771f\u4e0e\u5426,\u82f9\u679c\u65e9\u5df2\u7ecf\u8d62\u4e86', u'\u6bd4\u91d1\u94b1\u66f4\u80ae\u810f', u'\u63a8\u8350\u516c\u4f17\u53f7:\u805a\u7126\u4f20\u5a92', u'\u964c\u964c\u5230\u5e97\u901a:\u4ea7\u54c1\u9a71\u52a8\u65b0\u578b\u5546\u4e1a\u6a21\u5f0f', u'\u767e\u5ea6\u4e16\u754c\u79fb\u52a8\u5b89\u5168\u4eae\u5927\u62db \u9ad8\u8c03\u5f00\u653e\u6280\u672f\u80fd\u529b', u'\u522b\u628a\u8ba8\u94b1\u5f53\u6210\u4f17\u7b79', u'\u5546\u6237\u4e3a\u4ec0\u4e48\u8981\u9009\u62e9\u767e\u5ea6\u76f4\u8fbe\u53f7', u'tk\u6559\u4e3b\u548c\u7384\u6b66\u5b9e\u9a8c\u5ba4', u'\u4e0d\u5149\u5f00\u653e,\u8fd8\u5f00\u6e90, \u767e\u5ea6\u79fb\u52a8\u5b89\u5168\u5e73\u53f0\u8fd9\u6b21\u73a9\u5927\u4e86']
    sagacitymac.urls = ['http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200688142&idx=1&sn=b0701d6bb633542955c37b44e425514e&3rd=MzA3MDU4NTYzMw==&scene=6#rd', 'http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200664712&idx=1&sn=9e6e9dd1fe595256d461e2ddd1fe8208&3rd=MzA3MDU4NTYzMw==&scene=6#rd', 'http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200651935&idx=1&sn=9efeaa7eb597a9fe6a7f1cce116b7a7e&3rd=MzA3MDU4NTYzMw==&scene=6#rd', 'http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200651935&idx=2&sn=42af76856c34a87ac69ded8d99a4f8e8&3rd=MzA3MDU4NTYzMw==&scene=6#rd', 'http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200641647&idx=1&sn=85b04cf6af6a936820d5d912f540eae2&3rd=MzA3MDU4NTYzMw==&scene=6#rd', 'http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200641647&idx=2&sn=9ff298d90990709818b96794dc8cc3a5&3rd=MzA3MDU4NTYzMw==&scene=6#rd', 'http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200634493&idx=1&sn=8dfeca7c1cc32eeb93c0b2c883c4a3e0&3rd=MzA3MDU4NTYzMw==&scene=6#rd', 'http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200634493&idx=2&sn=4fba7fecdde2c82a78944d1c0e43e0d2&3rd=MzA3MDU4NTYzMw==&scene=6#rd', 'http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200630491&idx=1&sn=2a54aa5e97bbc9847f9480e0bc2b657d&3rd=MzA3MDU4NTYzMw==&scene=6#rd', 'http://mp.weixin.qq.com/s?__biz=MjM5MTc2MDEzMw==&mid=200598189&idx=1&sn=9cfa62dfbd498a622258ad0ce7245da0&3rd=MzA3MDU4NTYzMw==&scene=6#rd']

    # sagacitymac.getTitleUrl(self.url)

    wz = user('wz', [sagacitymac])
    wz.checkList()

