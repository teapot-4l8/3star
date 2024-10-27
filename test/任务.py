
import os
import requests
import hashlib
import time
import random


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
    resp = requests.post('https://xcx.vipxufan.com/star/apix171/signJob',headers=headers,data=data,verify=False)
    print(resp.text)


def chaohua():
    """
    微博超话发帖
    :return: {"status":200,"data":0,"msg":"请输入正确的超话链接哦","err":null}
    {"status":200,"data":0,"msg":"该链接已被领取过了","err":null}
    {"status":200,"data":{"status":1,"msg":"快来wx小橙序『五号星球』一起为爱心公益助力，我们在[给你小心心]XX星球[给你小心心]等你哦~"},"msg":"","err":""}
    """

    data = {
        'type': '0',
        'url': 'https://m.weibo.cn/detail/5092405743453302',  # https://m.weibo.ccn/7796346942/5092407916103268
        'uid': uid,
        'xid': '171',
    }

    response = requests.post('https://xcx.vipxufan.com/star/apix171/checkChaoHua', headers=headers, data=data)
    print(response.text)


def view_video():
    """
    看傻逼的广告
    :return:
    {"status":200,"data":{"is_view":1,"num":5,"rank":1,"total_num":5,"msg":"ok"},"msg":"ok","err":null}
    {"status":200,"data":{"is_view":0,"num":5,"rank":1,"total_num":5,"msg":"ok"},"msg":"ok","err":null}  看完次之后会提示的
    {"status":200,"data":{"is_view":0},"msg":"ok","err":"no"}

    {"status":200,"data":{"cishu":1,"num":2,"rank":1,"total_num":5,"msg":"ok"},"msg":"ok","err":null}
    {"status":200,"data":{"cishu":0,"num":2,"rank":1,"total_num":5,"msg":"ok"},"msg":"ok","err":null}
    {"status":0,"data":null,"msg":null,"err":"次数已经用完"}
    """
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
        resp = requests.post(url, headers=headers, data=data, verify=False)
        time.sleep(1)
        print(resp.text)

    data["type"] = "1"
    for i in range(3):
        resp = requests.post(url, headers=headers, data=data, verify=False)
        time.sleep(1)
        print(resp.text)

def xiaochengxu():
    """
    体验小程序x2
    :return: {"status":200,"data":{"num":5,"msg":"ok"},"msg":"ok","err":null}
    """
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


def choujinag():
    """
    抽奖任务，3次，务上显示4次，实际上只能抽三次，再多就要看视频。视频最多看3次。也就是每天有6次抽奖机会
    :return:
    {"status":200,"data":{"rank":"","times":1,"angle":90,"content":{"id":2,"name":"5克能量","desc":"能量","valid_num":0,"type":2,"rank":90,"water":5}},"msg":"ok","err":null}
    """
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
        resp = requests.post(url=url, headers=headers, data=data, verify=False)
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

def water():  # 有点奇怪 没有找到能量个数
    time_stamp, random_str, signature = a(uid)
    data = {
        'uid': uid,
        'xid': '171',
        'v': '2',
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }

    response = requests.post('https://xcx.vipxufan.com/star/apix171/water', headers=headers, data=data, verify=False)
    print(response.text)


if __name__ == '__main__':
    uid = os.environ["uid"]
    signJob()  # TODO 签到挑战
    # chaohua()  # TODO 微博爬取一个放进来
    view_video()
    xiaochengxu()
    choujinag()
    getjob()  # 抽奖4次就能领取
    water()  # 使用能量