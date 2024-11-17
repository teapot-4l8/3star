# -*- coding: utf-8 -*-
# @Time    : 2024/11/7 14:16
# @Desc    : 多账户同时挂机测试
import asyncio
import re

import aiohttp
import hashlib
import random
import time

from account import uid_list
from weibo import send_chaohua_async_request, send_chaohua_request


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
        self.uid = uid
        self.highest_num = 0
        self.auto_num = 1
        self.assist_times = 0  # 为别人助力次数
        self.be_assisted_times = 0  # 别人为我助力的次数

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

    async def post_request(self, url, data, session):
        """通用的异步POST请求方法"""
        async with session.post(url, headers=self.headers, data=data) as resp:
            return await resp.json()

    async def start(self):
        for i in range(5):
            await asyncio.sleep(2)  # 使用 asyncio.sleep 代替 time.sleep
            print(f"{self.uid} is doing task ...")

        print(f"{self.uid} finished !!!")


    async def signJob(self, session):
        print("\n===============签到==================")
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
        resp = await self.post_request('https://xcx.vipxufan.com/star/apix171/signJob', data, session)
        print(resp.text)

        continuous_sign_num = await self.check_signList()
        if continuous_sign_num:
            data.__delitem__("type")
            data['id'] = continuous_sign_num
            time_stamp, random_str, signature = self.a()
            data.update({"timeStamp": time_stamp, "randomStr": random_str, "signature": signature})
            res = await self.post_request('https://xcx.vipxufan.com/star/apix171/signJob', data, session)
            print(res.text)
        print()

    async def check_signList(self):
        data = {
            'uid': self.uid,
            'xid': '171',
        }
        continuous_sign_num = 0
        resp = await self.post_request('https://xcx.vipxufan.com/star/apix171/signList', data)
        sign_job = resp.json()['data']['sign_job']
        for s in sign_job:
            if s['status'] == 1:
                continuous_sign_num = s['id']

        return continuous_sign_num

    async def do_every_day_task(self):
        # tasks = [self.signJob, self.chaohua, self.view_video, self.xiaochengxu, self.choujiang, self.getjob]
        tasks = [self.chaohua]
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*(task(session) for task in tasks))


    async def chaohua(self, session):  # TODO 逻辑有误
        global since_id
        print(f"since_id====> {since_id}")
        while True:  # 一直尝试取链接，直到成功为止
            cards, since_id = send_chaohua_request()
            if not cards:  # 如果没有返回的cards，结束循环
                print("没有更多的内容可供翻页。")
                break
            for card in cards:
                try:
                    mblog = card['mblog']
                    text = mblog['text']
                    id_ = mblog['id']
                    target_page_url = "https://m.weibo.cn/detail/" + id_
                    if bool(re.search(r'『五号星球』', text)):
                        data = {
                            'type': '0',
                            'url': target_page_url,
                            'uid': self.uid,
                            'xid': '171',
                        }
                        resp_json = await self.post_request('https://xcx.vipxufan.com/star/apix171/checkChaoHua', data, session)
                        print(resp_json)
                        return resp_json['data']
                except KeyError:
                    pass
            print("target link not found in this loop")

    async def view_video(self, session):
        print("\n===============看视频5+3次==================")
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
            resp_json = await self.post_request(url, data, session)
            print(resp_json)
            if not resp_json["data"]["is_view"]:
                break

        data["type"] = "1"
        for i in range(3):
            resp_json = await self.post_request(url, data, session)
            print(resp_json)
            if not resp_json['status']:
                break

    async def xiaochengxu(self, session):
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

        resp_json = await self.post_request(url, data, session)
        if not resp_json["status"]:
            return
        data["appId"] = "wxa501c36b93761f58"
        resp_json = await self.post_request(url, data, session)
        print(resp_json)

    async def choujiang(self, session):
        print("\n===============抽奖6次==================")
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
            resp_json = await self.post_request(url, data, session)
            print(resp_json)
            if not resp_json["data"]:
                break

    async def getjob(self, session):  # TODO 看看是哪个接口
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

        resp_json = await self.post_request('https://xcx.vipxufan.com/star/apix171/getjob', data, session)
        print(resp_json)


async def start_task(uid, delay):
    await asyncio.sleep(delay)  # 等待指定的延迟时间
    ts = ThreeStar(uid)
    await ts.do_every_day_task()


async def main():
    total_time = 13  # 总时间（秒）
    num_uids = len(uid_list)  # uid的个数
    if num_uids == 0:
        print("No uids to process.")
        return

    interval = total_time / (num_uids - 1)  # 计算每个任务之间的间隔时间
    tasks = []
    for i, uid in enumerate(uid_list):
        delay = interval * i  # 计算每个任务的延迟时间
        task = start_task(uid, delay)
        tasks.append(task)

    # tasks = [ThreeStar(uid).do_every_day_task() for uid in uid_list]
    # 并发运行所有任务
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    since_id = None
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
