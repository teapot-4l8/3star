import requests
import hashlib
import time
import random
import os
import re

from account import uid_list

class ThreeStar:
    def __init__(self, uid):
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
        # self.uid = os.environ["uid"]
        self.uid = uid
        self.highest_num, self.auto_num = self.get_basic_info()


    def a(self):
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

        s = str(int(a)) + o + "meida123456" + self.uid
        e = hex_md5(s)
        e = hex_md5(e)
        return a, o, e

    def start(self):
        self.do_every_day_task()
        print("每日任务完成")
        total_num = int(self.highest_num / self.auto_num)
        print(f"循环次数=>{total_num}")
        print(f"需要{total_num * 13 / 60}分钟")
        for i in range(total_num):
            msg = self.validsave()
            if msg:
                break
            time.sleep(13)

    def do_every_day_task(self):
        self.signJob()
        self.chaohua()
        self.view_video()
        self.xiaochengxu()
        self.choujinag()
        self.getjob()

    def signJob(self):
        time_stamp, random_str, signature = self.a()
        data = {
            "type": "1",
            "uid": self.uid,
            "xid": "171",
            "v": "2",
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }
        resp = requests.post('https://xcx.vipxufan.com/star/apix171/signJob', headers=self.headers, data=data)
        print(resp.text)

    def chaohua(self):
        url = self.weibo_crawler()
        data = {
            'type': '0',
            'url': url,
            'uid': self.uid,
            'xid': '171',
        }

        response = requests.post('https://xcx.vipxufan.com/star/apix171/checkChaoHua', headers=self.headers, data=data)
        print(response.text)

    def view_video(self):
        time_stamp, random_str, signature = self.a()
        url = "https://xcx.vipxufan.com//star/apix171/viewVideo"
        data = {
            "uid": self.uid,
            "xid": "171",
            "v": "2",
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }

        for i in range(5):
            resp = requests.post(url, headers=self.headers, data=data)
            print(resp.text)

        data["type"] = "1"
        for i in range(3):
            resp = requests.post(url, headers=self.headers, data=data)
            print(resp.text)

    def xiaochengxu(self):
        url = "https://xcx.vipxufan.com//star/apix171/appjob"
        time_stamp, random_str, signature = self.a()
        data = {
            "appId": "wx3d7f3ea7e3793fa3",  # "大屏投放"小程序
            "uid": self.uid,
            "xid": "171",
            "v": "2",
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }

        resp = requests.post(url=url, headers=self.headers, data=data)
        print(resp.text)
        data["appId"] = "wxa501c36b93761f58"
        resp = requests.post(url=url, headers=self.headers, data=data)
        print(resp.text)

    def choujinag(self):
        time_stamp, random_str, signature = self.a()
        url = "https://xcx.vipxufan.com/star/apix171/lotteryWeb"
        data = {
            "angle": "0",
            "uid": self.uid,
            "xid": "171",
            "v": "2",
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }
        for i in range(6):
            resp = requests.post(url=url, headers=self.headers, data=data)
            print(resp.text)

    def getjob(self):
        time_stamp, random_str, signature = self.a()
        data = {
            'id': '3',
            'uid': self.uid,
            'xid': '171',
            'v': '2',
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }

        response = requests.post('https://xcx.vipxufan.com/star/apix171/getjob', headers=self.headers, data=data)
        print(response.text)

    def validsave(self):
        url = "https://xcx.vipxufan.com/star/apix171/validSave"
        data = {
            "uid": self.uid,
            "xid": "171"
        }

        resp = requests.post(url, headers=self.headers, data=data)
        print(resp.json())
        msg = resp.json()["msg"]
        return msg

    def get_basic_info(self):
        """
        获取基本信息，如每天最高的个数，一次能拿多少钻石
        :return:
        """
        data = {
            'uid': self.uid,
            'xid': '171',
        }

        response = requests.post('https://xcx.vipxufan.com/star/apix171/getIndex', headers=self.headers, data=data)
        # print(response.text)
        user_info = response.json()["data"]["user_info"]
        # print(user_info)
        valid_num = user_info["valid_num"]  # 剩余钻石数量
        rank = response.json()["data"]["rank"]
        highest_num = rank["highest_num"]  # 每天最多获取钻石shu
        auto_num = rank["auto_num"]  # 30秒自动增加的钻石数
        return highest_num, auto_num

    def validNum(self):
        url = "https://xcx.vipxufan.com/star/apix171/validNum"
        time_stamp, random_str, signature = self.a()
        data = {
            "num": self.highest_num,
            "uid": self.uid,
            "xid": "171",
            "v": "2",
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }

        resp = requests.post(url, headers=self.headers, data=data)
        print(resp.text)

    def weibo_crawler(self) -> str:
        DOMAIN = "https://m.weibo.cn/detail/"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'mweibo-pwa': '1',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://m.weibo.cn/p/index?extparam=%E8%82%96%E5%AE%87%E6%A2%81&containerid=100808abb887d7734e4121eef9853b451c11b9&luicode=20000061&lfid=5095189509047708',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrf-token': '5fa3ae',
        }
        params = {
            'extparam': '肖宇梁',
            'containerid': '100808abb887d7734e4121eef9853b451c11b9',
            # 'luicode': '20000061',
            # 'lfid': '5095189509047708',
        }
        response = requests.get('https://m.weibo.cn/api/container/getIndex', params=params, headers=headers)
        cards = response.json()['data']['cards']
        for card in cards:
            try:
                mblog = card['mblog']
                text = mblog['text']
                id_ = mblog['id']
                target_page_url = DOMAIN + id_
                if bool(re.search(r'『五号星球』', text)):
                    return target_page_url
            except KeyError:
                pass
        return ""


    def invite(self):
        time_stamp, random_str, signature = self.a()
        data = {
            'uid': self.uid,  # "我"
            'xid': '171',
            'jid': '3b262ba5d4780d79e54716d7aa03f890',  # "别人"
            'v': '2',
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }

        response = requests.post('https://xcx.vipxufan.com/star/apix171/invite', headers=self.headers, data=data)
        print(response.text)


if __name__ == '__main__':
    ts = ThreeStar(os.environ["uid"])
    ts.start()