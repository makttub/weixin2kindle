#!/usr/bin/python
#coding: utf-8

import account
import users
import mk
import send

mintshow = account.pubAccount('人生如戏', 'http://weixin.sogou.com/gzh?openid=oIWsFt1FSztdLmdVbgYcZFJ8p9Fg')
sagacitymac = account.pubAccount('MacTalk By 池建强', 'http://weixin.sogou.com/gzh?openid=oIWsFt98u7kmyb9-OpSPghHa7Uiw')
duhaoshu = account.pubAccount('十点读书', 'http://weixin.sogou.com/gzh?openid=oIWsFt8VjHhzC5aIcBZNCl-xB0Ec')
foodtonight = account.pubAccount('深夜谈吃', 'http://weixin.sogou.com/gzh?openid=oIWsFtyLnSV3VrDZ_07e5zMbwvqw')
doubanshiqing = account.pubAccount('豆瓣事情', 'http://weixin.sogou.com/gzh?openid=oIWsFt4mR3qSAa6We96X5EiCbRZY')
seniorplayer = account.pubAccount('大玩家 by 张磊', 'http://weixin.sogou.com/gzh?openid=oIWsFt3sSJFYcdEcqQeePTe55UEM')
everydayfunengliang = account.pubAccount('每天一波负能量', 'http://weixin.sogou.com/gzh?openid=oIWsFtyBF0HuXRmKsl3jGJfckjRY')
lazythought = account.pubAccount('懒人在思考', 'http://weixin.sogou.com/gzh?openid=oIWsFtwo1az2FajUL609KV51jhrM')
taobaoguijiaoqi = account.pubAccount('鬼脚七', 'http://weixin.sogou.com/gzh?openid=oIWsFt2QQkOK0nDUqZzOvdkm3Ch4')
today_inspire = account.pubAccount('今日', 'http://weixin.sogou.com/gzh?openid=oIWsFtw-UpWgDR1FfxAvjJFNWmD8')
sanbiao1984 = account.pubAccount('三表龙门阵', 'http://weixin.sogou.com/gzh?openid=oIWsFty72GGlJl1Fa32fnPqybPV8')
speedweekly = account.pubAccount('速度周刊', 'http://weixin.sogou.com/gzh?openid=oIWsFt0ywvBlyiY4YxcZ-65kFqQo')
douban = account.pubAccount('豆瓣', 'http://weixin.sogou.com/gzh?openid=oIWsFt0ywvBlyiY4YxcZ-65kFqQo')
shaoxizhi214 = account.pubAccount('邵皙智工作室', 'http://weixin.sogou.com/gzh?openid=oIWsFtxpswbhJmMEeqzLhikQBzPc')
zenpark = account.pubAccount('精进学堂', 'http://weixin.sogou.com/gzh?openid=oIWsFt3VWonT9PvhnPyOGiTinHlk')
JulesandJim = account.pubAccount('法外之徒', 'http://weixin.sogou.com/gzh?openid=oIWsFt03yb4SrUnI1ihKKXRym4Us')
drink_oh_yeah = account.pubAccount('猎酒党', 'http://weixin.sogou.com/gzh?openid=oIWsFt-5RQHelxMU4k0zm3yx_x_8')
fakecountry = account.pubAccount('花家舍', 'http://weixin.sogou.com/gzh?openid=oIWsFt2kv0vULsU3ROdZgEZwts54')
taosay = account.pubAccount('道哥的黑板报', 'http://weixin.sogou.com/gzh?openid=oIWsFty5GrTq6kuv7Ny-PhQSOQh0')
tencent_blackboard = account.pubAccount('腾讯黑板报', 'http://weixin.sogou.com/gzh?openid=oIWsFt23D0QFnnZq3cjK3IDktk9c')
baibanbaonet = account.pubAccount('白板报', 'http://weixin.sogou.com/gzh?openid=oIWsFt-1VrJXMHgB-JB3iNhMcZ4M')
it_spy = account.pubAccount('IT八卦', 'http://weixin.sogou.com/gzh?openid=oIWsFty3AlNGjSB31Y-nSs5NGNhs')





wz = users.user('wz', 'lwwz1990@kindle.com', [mintshow, sagacitymac, duhaoshu, foodtonight,
                                                doubanshiqing, seniorplayer, everydayfunengliang,
                                                lazythought, taobaoguijiaoqi, today_inspire, sanbiao1984,
                                                speedweekly, douban, shaoxizhi214, zenpark,
                                                JulesandJim, drink_oh_yeah, fakecountry, taosay, tencent_blackboard,
                                                baibanbaonet, it_spy])

if wz.checkList():
    mk.mkmobi(wz)
    send.send(wz)
