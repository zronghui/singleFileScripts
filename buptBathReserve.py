#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime, timedelta
from sendQQMail import mail
from loguru import logger

cookies = {
    'laravel_session': open('./bathCookie.txt').read().strip().split('=')[1],
}

headers = {
    'Content-Length': '30',
    'Origin': 'http://wx.bupt.edu.cn',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/2.4.2(0x12040212) NetType/WIFI WindowsWechat',
    'Host': 'wx.bupt.edu.cn',
    'Referer': 'http://wx.bupt.edu.cn/bathroom/index',
    'Accept-Language': 'zh-cn',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
}


def tomorrow():
    return (datetime.now() + timedelta(days=1)).isoformat().split('T')[0]


def successReserveTomorrow(r):
    return r.status_code == 200 and '取消明日预约' in r.text


def bathroomSubmit(data):
    return requests.post('http://wx.bupt.edu.cn/bathroom/submit', headers=headers, cookies=cookies, data=data)


def main():
    logger.add('buptBathReserve.log')
    data = {
        # 'period': '2020-09-03 22:20:00'
        'period': tomorrow() + ' 22:20:00'
    }
    if datetime.now().hour == 8:
        while True:
            r = bathroomSubmit(data)
            if successReserveTomorrow(r):
                break
            logger.debug(r.status_code)
        logger.debug(r.status_code, r.text)
        mail('buptBathReverse', f'{r.status_code} 预约成功', r.text)
    else:
        # 不在 8 点，检查 cookie 是否有效
        r = bathroomSubmit(data)
        if not successReserveTomorrow(r):
            mail('buptBathReverse', f'{r.status_code} 请检查cookie', r.text)
            logger.debug(f'{r.status_code} 请检查cookie')
            logger.debug(r.text)
        else:
            logger.debug('当前 cookie 仍有效')


if __name__ == "__main__":
    main()
