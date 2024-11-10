# -*- coding: utf-8 -*-
# @Author  : chaiyunze@gmail.com
# @Time    : 2024/10/27 9:57
# @Desc    :
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


def send_get_request():
    response = requests.get('https://m.weibo.cn/api/container/getIndex', params=params,headers=headers)
    # print(response.json())
    data = response.json()['data']
    cards = data['cards']
    # print(cards)
    since_id = data['pageInfo']['since_id']
    return cards, since_id

def is_target(text):
    return bool(re.search(r'『五号星球』', text))  # 检查text中是否包含"『五号星球』"

def parse_response(card):
    mblog = card['mblog']
    created_at = mblog['created_at']
    text = mblog['text']
    id_ = mblog['id']
    target_page_url = DOMAIN + id_
    if is_target(text):
        print(created_at)
        print(text)
        print(id_)
        print(target_page_url)
        print("=============================================")


if __name__ == '__main__':
    params = {
        'extparam': '肖宇梁',
        'containerid': '100808abb887d7734e4121eef9853b451c11b9',
        # 'luicode': '20000061',
        # 'lfid': '5095189509047708',
        # "since_id": "5099143848529594"  # 靠这里翻页
    }
    cards, since_id = send_get_request()
    for card in cards:
        try:
            parse_response(card)
        except KeyError:
            pass
