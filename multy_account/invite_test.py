# -*- coding: utf-8 -*-
# @Time    : 2024/11/6 11:46
# @Desc    : 测试多人助力逻辑
import hashlib

import requests

from account import uid_list
import os
import random
import time


class ThreeStar:
    def __init__(self, uid):
        self.uid = uid
        self.headers = {
            "host": "xcx.vipxufan.com",
            "xweb_xhr": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b)XWEB/11275",
            "accept": "*/*",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://servicewechat.com/wxc86124c201e9b259/11/page-frame.html",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "gzip, deflate, br"
        }
        self.remain_assist_times = 3  # 为别人助力次数
        self.remain_assisted_times = 6  # 别人为我助力的次数
        self.assisted_by = set()  # 记录哪些uid已经为我助力过

    def post_request(self, url, data):
        """通用的POST请求方法"""
        resp = requests.post(url, headers=self.headers, data=data)
        # print(resp.text)
        return resp

    def a(self):
        t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        i = random.randint(0, len(t))
        if i > len(t) - 9:
            i = len(t) - 9
        o = t[i:i + 8]
        a = time.time() * 1000

        def hex_md5(data):
            m = hashlib.md5()
            m.update(data.encode())
            return m.hexdigest()

        s = str(int(a)) + o + "meida123456" + self.uid
        e = hex_md5(s)
        e = hex_md5(e)
        return a, o, e


    def assist_jid(self, jid):
        # 发送网络请求检查助力是否成功
        response = self.check_assist(jid)
        if response["status"] == 200 and response["data"]["status"] == 1:
            self.remain_assist_times -= 1
            print(f"{self.uid} assist {jid}, assist_times remain {self.remain_assist_times}")
        elif response["status"] == 0 and "已达上限" in response["msg"]:
            self.remain_assist_times = 0
            print(f"{self.uid} has reached the maximum assist times and is now locked.")
        else:
            print(f"Assist failed for {jid}, msg: {response['msg']}")

    def check_assist(self, jid):
        time_stamp, random_str, signature = self.a()
        data = {
            'uid': self.uid,  # "我"
            'xid': '171',
            'jid': jid,  # "别人"
            'v': '2',
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }

        resp = self.post_request('https://xcx.vipxufan.com/star/apix171/invite', data)
        print(resp.text)
        return resp.json()

    def assisted(self):
        if self.remain_assisted_times > 0:
            self.remain_assisted_times -= 1
            print(f"{self.uid} has been assisted, remain_assisted_times left: {self.remain_assisted_times}")
        else:
            print(f"{self.uid} has reached the maximum assisted times.")


if __name__ == '__main__':
    # 创建账号实例
    ts_accounts = {uid: ThreeStar(uid) for uid in uid_list}

    # 模拟助力过程
    for i in range(len(uid_list)):
        for j in range(len(uid_list)):
            if i != j and ts_accounts[uid_list[i]].remain_assist_times > 0:
                ts_accounts[uid_list[i]].assist_jid(uid_list[j])

    # 打印每个账号的助力情况
    for uid, ts in ts_accounts.items():
        print(f"{ts.uid} has {ts.remain_assist_times} assist times left and has been assisted {ts.remain_assisted_times} times.")