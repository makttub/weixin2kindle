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
            conn.text_factory = str
            cursor = conn.cursor()

            for i in range(len(self.accounts)):
                deltitles = []
                for title in self.accounts[i].titleUrl:
                    cursor.execute('select * from send where title=?', (title,))
                    result = cursor.fetchall()
                    if len(result) != 0:
                        deltitles.append(title)
                    else:
                        cursor.execute("insert into send values ('%s','%s','%s')" % (self.accounts[i].name, title, self.accounts[i].titleUrl[title]))
                for title in deltitles:
                    self.accounts[i].titleUrl.pop(title)
        finally:
            cursor.close()
            conn.commit()
            conn.close()


    def mkTable(self):
        try:
            dbdir = os.path.join(self.dirpath, 'sended.db')
            conn = sqlite3.connect(dbdir)
            cursor = conn.cursor()
            cursor.execute('create table if not exists send (account varchar(20), title str not null, url str not null)')
        finally:
            cursor.close()
            conn.commit()
            conn.close()

if __name__ == '__main__':
    mintshow = account.pubAccount('mintshow', u'http://weixin.sogou.com/gzh?openid=oIWsFt1FSztdLmdVbgYcZFJ8p9Fg')
    sagacitymac = account.pubAccount('sagacitymac', u'http://weixin.sogou.com/gzh?openid=oIWsFt98u7kmyb9-OpSPghHa7Uiw')

    wz = user('wz', [mintshow, sagacitymac])
    wz.checkList()

