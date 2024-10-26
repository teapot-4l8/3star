import requests
import os

def log_in():
    url = "https://xcx.vipxufan.com/star/apix171/login"
    headers = {
        "connection": "keep-alive",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.06.2209190 MicroMessenger/8.0.5 Language/zh_CN webview/",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://servicewechat.com/wx6b6da4e842c89b90/devtools/page-frame.html",
        "accept-encoding": "gzip, deflate, br"
    }
    data = {
        "code": os.environ["code"],  # 这里出的问题
        "xid": "171"
    }

    with requests.post(url=url, headers=headers, data=data, verify=False) as resp:
        resp.raise_for_status()
        print(resp.text)



def get_code():
    url = "https://servicewechat.com/wxa-dev-logic/jslogin?_r=0.5017947553947279&newticket=Ut8cKsaT7CVs_g0Q4-N5araal0h_E-HjGSmLW8ltPC0&appid=wxc86124c201e9b259&platform=0&ext_appid=&os=win&clientversion=1022004020"
    headers = {
        "host": "servicewechat.com",
        "content-length": "25",
        "Connection": "close",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.3 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 wechatdevtools/1.06.2209190 MicroMessenger/8.0.5 Language/zh_CN webview/",

    }
    resp = requests.post(url, headers=headers)
    print(resp.text)


if __name__ == '__main__':
    # log_in()
    get_code()