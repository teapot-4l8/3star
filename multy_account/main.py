import requests
import hashlib
import time
import random
import os
import re

from account import uid_list

class ThreeStar:
    def __init__(self, uid):
        self.diamonds_num = 0
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
        self.diamonds_num = self.check_diamonds_num()
        self.validNum()

    def do_every_day_task(self):
        tasks = [self.signJob, self.chaohua, self.view_video, self.xiaochengxu, self.choujinag, self.getjob]
        for task in tasks:
            task()

    def post_request(self, url, data):
        """通用的POST请求方法"""
        resp = requests.post(url, headers=self.headers, data=data)
        # print(resp.text)
        return resp

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
        resp = self.post_request('https://xcx.vipxufan.com/star/apix171/signJob', data)
        print(resp.text)

        continuous_sign_num = self.check_signList()
        if continuous_sign_num:
            data.__delitem__("type")
            data['id'] = continuous_sign_num
            time_stamp, random_str, signature = self.a()
            data.update({"timeStamp": time_stamp, "randomStr": random_str, "signature": signature})
            resp = self.post_request('https://xcx.vipxufan.com/star/apix171/signJob', data)
            print(resp.text)

    def chaohua(self):
        url = self.weibo_crawler()
        data = {
            'type': '0',
            'url': url,
            'uid': self.uid,
            'xid': '171',
        }

        resp = self.post_request('https://xcx.vipxufan.com/star/apix171/checkChaoHua', data)
        print(resp.text)

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
            resp = self.post_request(url, data)
            print(resp.text)

        data["type"] = "1"
        for i in range(3):
            resp = self.post_request(url, data)
            print(resp.text)

    def xiaochengxu(self):
        url = "https://xcx.vipxufan.com//star/apix171/appjob"
        time_stamp, random_str, signature = self.a()
        data = {
            "appId": "wx3d7f3ea7e3793fa3",
            "uid": self.uid,
            "xid": "171",
            "v": "2",
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }

        resp = self.post_request(url, data)
        print(resp.text)
        data["appId"] = "wxa501c36b93761f58"
        resp = self.post_request(url, data)
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
            resp = self.post_request(url, data)
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

        resp = self.post_request('https://xcx.vipxufan.com/star/apix171/getjob', data)
        print(resp.text)

    def validsave(self):
        url = "https://xcx.vipxufan.com/star/apix171/validSave"
        data = {
            "uid": self.uid,
            "xid": "171"
        }

        resp = self.post_request(url, data)
        print(resp.json())
        msg = resp.json()["msg"]
        return msg

    def get_basic_info(self):
        data = {
            'uid': self.uid,
            'xid': '171',
        }

        resp = self.post_request('https://xcx.vipxufan.com/star/apix171/getIndex', data)
        user_info = resp.json()["data"]["user_info"]
        rank = resp.json()["data"]["rank"]
        highest_num = rank["highest_num"]
        auto_num = rank["auto_num"]
        return highest_num, auto_num

    def validNum(self):
        url = "https://xcx.vipxufan.com/star/apix171/validNum"
        time_stamp, random_str, signature = self.a()
        data = {
            "num": self.diamonds_num,
            "uid": self.uid,
            "xid": "171",
            "v": "2",
            "timeStamp": time_stamp,
            "randomStr": random_str,
            "signature": signature
        }

        resp = self.post_request(url, data)
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

        resp = self.post_request('https://xcx.vipxufan.com/star/apix171/invite', data)
        print(resp.text)

    def check_diamonds_num(self):
        data = {
            'uid': self.uid,
            'xid': '171',
        }
        resp = self.post_request('https://xcx.vipxufan.com/star/apix171/getIndex',data=data)
        user_info = resp.json()["data"]["user_info"]
        rank_num = user_info["rank_num"]
        return rank_num

    def check_signList(self):
        data = {
            'uid': self.uid,
            'xid': '171',
        }
        continuous_sign_num = 0
        resp = self.post_request('https://xcx.vipxufan.com/star/apix171/signList', data)
        sign_job = resp.json()['data']['sign_job']
        for s in sign_job:
            if s['status'] == 1:
                continuous_sign_num = s['id']

        return continuous_sign_num


if __name__ == '__main__':
    ts = ThreeStar(os.environ["uid"])
    ts.start()