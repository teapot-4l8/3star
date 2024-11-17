# -*- coding: utf-8 -*-
# @Author  : chaiyunze@gmail.com
# @Time    : 2024/10/27 9:57
# @Desc    :
import aiohttp
import requests
import re

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

def send_chaohua_request(since_id=None):
    params = {
        'extparam': '肖宇梁',
        'containerid': '100808abb887d7734e4121eef9853b451c11b9',
    }
    if since_id:
        params["since_id"] = since_id  # 如果有since_id，则添加到请求参数中

    response = requests.get('https://m.weibo.cn/api/container/getIndex', params=params, headers=headers)
    data = response.json()['data']
    cards = data['cards']
    since_id = data['pageInfo']['since_id']  # 获取新的since_id
    return cards, since_id


async def send_chaohua_async_request(since_id=None):
    params = {
        'extparam': '肖宇梁',
        'containerid': '100808abb887d7734e4121eef9853b451c11b9',
    }
    if since_id:
        params["since_id"] = since_id  # 如果有since_id，则添加到请求参数中

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get('https://m.weibo.cn/api/container/getIndex', params=params) as resp:
            data = await resp.json()
            print(data)
            cards = data['data']['cards']
            since_id = data['data']['pageInfo']['since_id']
            return cards, since_id


def weibo_crawler():
    while True:
        cards, since_id = send_chaohua_request()  # 发送请求并获取cards和since_id
        if not cards:  # 如果没有返回的cards，结束循环
            print("没有更多的内容可供翻页。")
            break
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
        print("target link not found in this loop")


if __name__ == '__main__':
    # since_id = None  # 初始化since_id为None
    print(weibo_crawler())