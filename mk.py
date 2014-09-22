#coding: utf-8

import users
import account
from datetime import *
import os
import commands
import json

def getTime():
    now = str(datetime.now())
    now = now.replace('-', '_')
    now = now.replace(' ', '_')
    now = now.replace(':', '_')
    now = now.replace('.', '_')
    return now

def mkmobi(u):
    timenow = getTime()
    recipepath = os.path.join(u.dirpath, timenow + '.recipe')
    with open(recipepath, 'w') as f:
        head = """from calibre.web.feeds.recipes import BasicNewsRecipe

class Git_Pocket_Guide(BasicNewsRecipe):

    title = 'Git Pocket Guide'
    description = ''

    no_stylesheets = True
    # keep_only_tags = [{ 'class': 'rich_media_content_wrp' }]

    def get_title(self, link):
        return link.contents[0].strip()

    def parse_index(self):
        ans = """
        book = []
        for i in range(len(u.accounts)):
            if len(u.accounts[i].titleUrl) != 0:
                chapters = []
                for title in u.accounts[i].titleUrl:
                    chapter = {}
                    chapter['url'] = u.accounts[i].titleUrl[title]
                    chapter['title'] = title
                    chapters.append(chapter)
                volume = (u.accounts[i].name, chapters)
                book.append(volume)

        tail = """        return ans
        """

        f.write(head + str(book) + '\n' + os.linesep + tail)

    shellCommands = 'ebook-convert ' + u.dirpath + os.sep + timenow + '.recipe ' + u.dirpath + os.sep + timenow + '.mobi'
    # print shellCommands
    print "ebook-convert..."
    if len(book) != 0:
        exitStatus, out = commands.getstatusoutput(shellCommands)
        logpath = os.path.join(u.dirpath, timenow + '.log')
        with open(logpath, 'w') as f:
            f.write(str(exitStatus))
            f.write(str(out))

if __name__ == '__main__':

    mintshow = account.pubAccount('人生如戏', u'http://weixin.sogou.com/gzh?openid=oIWsFt1FSztdLmdVbgYcZFJ8p9Fg')
    sagacitymac = account.pubAccount('MacTalk By 池建强', u'http://weixin.sogou.com/gzh?openid=oIWsFt98u7kmyb9-OpSPghHa7Uiw')

    wz = users.user('wz', [mintshow, sagacitymac])
    wz.checkList()
    mkmobi(wz)
