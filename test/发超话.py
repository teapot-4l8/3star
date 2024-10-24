import requests
import os

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
}

data = {
    'type': '0',
    'url': 'https://gitee.com/teapot_418/660-archive/raw/master/m.weibo.cn/status/5093102488915015.html',
    'uid': os.environ["uid"],
    'xid': '171',
}

response = requests.post('https://xcx.vipxufan.com/star/apix171/checkChaoHua', headers=headers, data=data)
print(response.text)