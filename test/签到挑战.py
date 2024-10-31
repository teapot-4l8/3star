# -*- coding: utf-8 -*-
# @Author  : chaiyunze@gmail.com
# @Time    : 2024/10/31 11:57
# @Desc    :
import hashlib
import os
import random
import time

import requests

headers = {
    'Host': 'xcx.vipxufan.com',
    'xweb_xhr': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b)XWEB/11275',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wxc86124c201e9b259/11/page-frame.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


def a(uid):
    t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    i = random.randint(0, len(t))
    if i > len(t) - 9:
        i = len(t) - 9
    o = t[i:i + 8]
    a = time.time() * 1000

    # 假设存在一个函数计算 MD5 的十六进制值，这里只是模拟
    def hex_md5(data):
        m = hashlib.md5()
        m.update(data.encode())
        return m.hexdigest()

    s = str(int(a)) + o + "meida123456" + uid
    e = hex_md5(s)
    e = hex_md5(e)
    return a, o, e


time_stamp, random_str, signature = a(os.environ["uid"])
data = {
    'id': '15',  # 连续签到天数
    'uid': os.environ["uid"],
    'xid': '171',
    'v': '2',
    "timeStamp": time_stamp,
    "randomStr": random_str,
    "signature": signature
}

response = requests.post('https://xcx.vipxufan.com/star/apix171/signJob', headers=headers, data=data, verify=False)
print(response.text)
