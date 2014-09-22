#coding: utf-8

import users
import account
from datetime import *
import os

def getTime():
    now = str(datetime.now())
    now = now.replace('-', '_')
    now = now.replace(' ', '_')
    now = now.replace(':', '_')
    now = now.replace('.', '_')
    return now

def mkrecipe(u):
    recipepath = os.path.join(u.dirpath, getTime() + '.recipe')
    with open(recipepath, 'w'):
        pass

if __name__ == '__main__':
    mintshow = account.pubAccount('人生如戏', u'http://weixin.sogou.com/gzh?openid=oIWsFt1FSztdLmdVbgYcZFJ8p9Fg')
    sagacitymac = account.pubAccount('MacTalk By 池建强', u'http://weixin.sogou.com/gzh?openid=oIWsFt98u7kmyb9-OpSPghHa7Uiw')

    wz = users.user('wz', [mintshow, sagacitymac])
    wz.checkList()
    mkrecipe(wz)
