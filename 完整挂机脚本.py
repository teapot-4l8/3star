import requests
import hashlib
import time
import random
import os
import re

headers = {
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

def validNum():
    url = "https://xcx.vipxufan.com/star/apix171/validNum"
    time_stamp, random_str, signature = a(uid)
    data = {
        "num": highest_num,
        "uid": uid,
        "xid": "171",
        "v": "2",
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }

    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)

def validsave():
    url = "https://xcx.vipxufan.com/star/apix171/validSave"
    data = {
        "uid": uid,
        "xid": "171"
    }

    resp = requests.post(url, headers=headers, data=data)
    print(resp.json())
    msg = resp.json()["msg"]
    return msg

def send_diamonds():
    url = "https://xcx.vipxufan.com/star/apix171/dahit"
    time_stamp, random_str, signature = a(uid)
    data = {
        "sid": "88",
        "number": highest_num,
        "type": "0",
        "uid": uid,
        "xid": "171",
        "v": "2",
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }

    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)

def signJob():
    """
    签到
    :return: {"status":200,"data":{"msg":"恭喜获得3钻石和1g能量","data":1,"number":3,"water":1},"msg":null,"err":"返回成功"}
    """
    time_stamp, random_str, signature = a(uid)
    data = {
        "type": "1",
        "uid": uid,
        "xid": "171",
        "v": "2",
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }
    resp = requests.post('https://xcx.vipxufan.com/star/apix171/signJob', headers=headers, data=data)
    print(resp.text)

def weibo_crawler() -> str:
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

def chaohua():
    url = weibo_crawler()
    data = {
        'type': '0',
        'url': url,
        'uid': uid,
        'xid': '171',
    }

    response = requests.post('https://xcx.vipxufan.com/star/apix171/checkChaoHua', headers=headers, data=data)
    print(response.text)

def view_video():
    time_stamp, random_str, signature = a(uid)
    url = "https://xcx.vipxufan.com//star/apix171/viewVideo"
    data = {
        "uid": uid,
        "xid": "171",
        "v": "2",
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }

    for i in range(5):
        resp = requests.post(url, headers=headers, data=data)
        # time.sleep(1)
        print(resp.text)

    data["type"] = "1"
    for i in range(3):
        resp = requests.post(url, headers=headers, data=data)
        # time.sleep(1)
        print(resp.text)

def choujinag():
    time_stamp, random_str, signature = a(uid)
    url = "https://xcx.vipxufan.com/star/apix171/lotteryWeb"
    data = {
        "angle": "0",
        "uid": uid,
        "xid": "171",
        "v": "2",
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }
    for i in range(6):
        resp = requests.post(url=url, headers=headers, data=data)
        print(resp.text)

def getjob():
    time_stamp, random_str, signature = a(uid)
    data = {
        'id': '3',
        'uid': uid,
        'xid': '171',
        'v': '2',
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }

    response = requests.post('https://xcx.vipxufan.com/star/apix171/getjob', headers=headers, data=data)
    print(response.text)

def water():
    time_stamp, random_str, signature = a(uid)
    data = {
        'uid': uid,
        'xid': '171',
        'v': '2',
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }

    response = requests.post('https://xcx.vipxufan.com/star/apix171/water', headers=headers, data=data)
    print(response.text)

def do_every_day_task():
    signJob()  # TODO 累计签到
    chaohua()  # TODO 超话自动翻页
    view_video()
    xiaochengxu()
    choujinag()
    getjob()
    # water()  # 可删去 让用户看到效果

def xiaochengxu():
    url = "https://xcx.vipxufan.com//star/apix171/appjob"
    time_stamp, random_str, signature = a(uid)
    data = {
        "appId": "wx3d7f3ea7e3793fa3",  # "大屏投放"小程序
        "uid": uid,
        "xid": "171",
        "v": "2",
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }

    resp = requests.post(url=url, headers=headers, data=data)
    print(resp.text)
    data["appId"] = "wxa501c36b93761f58"
    resp = requests.post(url=url, headers=headers, data=data)
    print(resp.text)

def get_basic_info():
    """
    获取基本信息，如每天最高的个数，一次能拿多少钻石
    :return:
    """
    data = {
        'uid': uid,
        'xid': '171',
    }

    response = requests.post('https://xcx.vipxufan.com/star/apix171/getIndex', headers=headers, data=data)
    # print(response.text)
    user_info = response.json()["data"]["user_info"]
    # print(user_info)
    valid_num = user_info["valid_num"]  # 剩余钻石数量
    rank = response.json()["data"]["rank"]
    highest_num = rank["highest_num"]  # 每天最多获取钻石shu
    auto_num = rank["auto_num"]  # 30秒自动增加的钻石数
    return highest_num, auto_num


def check_diamonds_num() -> int:
    pass


if __name__ == '__main__':  # TODO print -> log
    uid = os.environ['uid']
    highest_num, auto_num = get_basic_info()
    do_every_day_task()
    print("每日任务完成")
    total_num = int(highest_num/auto_num)
    print(f"循环次数=>{total_num}")
    print(f"需要{total_num * 13 / 60}分钟")
    for i in range(total_num):
        msg = validsave()
        if msg:
            break
        # validNum()
        # send_diamonds()
        time.sleep(13)

    # TODO 检查前端钻石总数，免得收走钻石的时候报错  找不到 :(
    # diamonds_num = check_diamonds_num()
    # validNum()  # 一次性收走所有产出的钻石
    # send_diamonds()  # 一次性将所有钻石存入xyl星球
