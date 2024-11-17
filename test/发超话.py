# import requests
# import os
#
# headers = {
#     'Host': 'xcx.vipxufan.com',
#     'xweb_xhr': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b)XWEB/11275',
#     'Accept': '*/*',
#     'Sec-Fetch-Site': 'cross-site',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Dest': 'empty',
#     'Referer': 'https://servicewechat.com/wxc86124c201e9b259/11/page-frame.html',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
# }
#
# data = {
#     'type': '0',
#     'url': 'https://gitee.com/teapot_418/660-archive/raw/master/m.weibo.cn/status/5093102488915015.html',
#     'uid': os.environ["uid"],
#     'xid': '171',
# }
#
# response = requests.post('https://xcx.vipxufan.com/star/apix171/checkChaoHua', headers=headers, data=data)
# print(response.text)



import requests

cookies = {
    'SCF': 'AlR5GlASD2s16zMbp25Ns5lNhbz3gh8EIHMnD2wL24pyxGHaxy-jsQYj9cdFKxYsSUpbOvuQKu2tzO9hnDuM7bs.',
    'SUB': '_2A25KNE3iDeRhGeFI7lsT9yfKzDuIHXVpSM8qrDV6PUJbktAGLU_7kW1NfRTY9GYwS_95q5YTT_u9xYkFrQTQjNOw',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5o5CK075rlJoB3yqHqmHi75JpX5KMhUgL.FoMcSK.ES0.cS0M2dJLoIEQLxK.LB.zL1KnLxKnLB--LBKBLxKqL1KnLBo-LxKMLBKMLBoW0IJx39gQt',
    'ALF': '1733806771',
    '_T_WM': '78966176304',
    'XSRF-TOKEN': 'a70764',
    'WEIBOCN_FROM': '1110006030',
    'MLOGIN': '1',
    'mweibo_short_token': 'eab705b170',
    'M_WEIBOCN_PARAMS': 'luicode%3D20000174%26lfid%3D100808abb887d7734e4121eef9853b451c11b9%26fid%3D100808abb887d7734e4121eef9853b451c11b9%26uicode%3D10000011',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'SCF=AlR5GlASD2s16zMbp25Ns5lNhbz3gh8EIHMnD2wL24pyxGHaxy-jsQYj9cdFKxYsSUpbOvuQKu2tzO9hnDuM7bs.; SUB=_2A25KNE3iDeRhGeFI7lsT9yfKzDuIHXVpSM8qrDV6PUJbktAGLU_7kW1NfRTY9GYwS_95q5YTT_u9xYkFrQTQjNOw; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5o5CK075rlJoB3yqHqmHi75JpX5KMhUgL.FoMcSK.ES0.cS0M2dJLoIEQLxK.LB.zL1KnLxKnLB--LBKBLxKqL1KnLBo-LxKMLBKMLBoW0IJx39gQt; ALF=1733806771; _T_WM=78966176304; XSRF-TOKEN=a70764; WEIBOCN_FROM=1110006030; MLOGIN=1; mweibo_short_token=eab705b170; M_WEIBOCN_PARAMS=luicode%3D20000174%26lfid%3D100808abb887d7734e4121eef9853b451c11b9%26fid%3D100808abb887d7734e4121eef9853b451c11b9%26uicode%3D10000011',
    'mweibo-pwa': '1',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://m.weibo.cn/p/index?extparam=%E8%82%96%E5%AE%87%E6%A2%81&containerid=100808abb887d7734e4121eef9853b451c11b9&luicode=20000174',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'a70764',
}

params = {
    'extparam': '肖宇梁',
    'containerid': '100808abb887d7734e4121eef9853b451c11b9',
    'luicode': '20000174',
}

response = requests.get('https://m.weibo.cn/api/container/getIndex', params=params, cookies=cookies, headers=headers)

print(response.text)

