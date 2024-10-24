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


def validNum():
    url = "https://xcx.vipxufan.com/star/apix171/validNum"
    time_stamp, random_str, signature = a(uid)
    data = {
        "num": "3",
        "uid": uid,
        "xid": "171",
        "v": "2",
        "timeStamp": time_stamp,
        "randomStr": random_str,
        "signature": signature
    }

    resp = requests.post(url, headers=headers, data=data, verify=False)
    print(resp.text)


def validsave():
    url = "https://xcx.vipxufan.com/star/apix171/validSave"
    data = {
        "uid": uid,
        "xid": "171"
    }

    resp = requests.post(url, headers=headers, data=data, verify=False)
    print(resp.text)


if __name__ == '__main__':
    import os
    uid = os.environ['uid']
    for i in range(36):
        validsave()  #                                            {"status":200,"data":null,"msg":200,"err":"今日已产满"}
        validNum()   # {"status":200,"data":1,"msg":null,"err":"返回成功"}  {"status":0,"data":null,"msg":"用户异常","err":"0"}
        time.sleep(13)

# num=9&uid=7740581754f9f09cb99dceebca95bde6&xid=171&v=2&timeStamp=1729254984360&randomStr=XYZ01234&signature=4f5627e83410a39fd2646679ac706061