
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
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'uid': '7740581754f9f09cb99dceebca95bde6',
    'xid': '171',
    'jid': '2ec2a70d7a8d71f4471ebedce547b37a',
    'v': '2',
    # 不验证
    'timeStamp': '1730611618872',
    'randomStr': 'PQRSTUVW',
    'signature': '3d4bf55226d031c1814061855b9e2878',
}

response = requests.post('https://xcx.vipxufan.com/star/apix171/invite', headers=headers, data=data, verify=False)
print(response.text)

"""
jid

7740581754f9f09cb99dceebca95bde6

2ec2a70d7a8d71f4471ebedce547b37a
f7fb9414a8904591c39a9e7933f78848
2ec2a70d7a8d71f4471ebedce547b37a
"""