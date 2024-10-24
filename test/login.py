import requests
import os
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
