#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

import pretty_errors
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
from alive_progress import alive_bar
from icecream import ic

pretty_errors.activate()

threadNum = 8  # 抢券线程数
interval = 0.1  # 失败重试间隔
secondsAhead = 1  # 提前几秒开始抢券
# 目前只支持整点抢券
coupons = [
    {
        'name': '伊利199-100',
        'time': '0/10',
        'command': './jd1.sh',
        'couponUrl': ''
    }
]


def qiangQuanThread(coupon):
    while True:
        now = time.strftime("%H:%M:%S")
        hour, minute, second = map(int, now.split(':'))
        if second in list(range(3, 30)):
            ic(coupon['name'], '抢券失败，已停止')
            break
        res = os.popen(coupon['command']).read()
        if '成功' in res:
            ic(coupon['name'], res)
            break
        time.sleep(interval)


def qiangQuan(coupon):
    with alive_bar(0) as bar:
        while True:
            while True:
                now = time.strftime("%H:%M:%S")
                hour, minute, second = map(int, now.split(':'))
                # 半点可以修改 minute in [29, 59]
                if minute == 59 and second in list(range(60 - secondsAhead, 60)):
                    next_hour = (hour + 1) % 24
                    if str(next_hour) in coupon['time'].split('/'):
                        break
                # 50分的时候检查登录状态
                if minute % 5 == second == 0:
                    res = os.popen(coupon['command']).read()
                    if 'not login' in res:
                        os.system('open https://plogin.m.jd.com/login/login')
                        os.system(f'open {coupon["couponUrl"]}; say "登录失效"')
                        return
                    print('登录状态有效')
                bar.text(f'waiting [process={os.getpid()}), name={coupon["name"]}]')
                time.sleep(1)
            pool = ThreadPool(processes=threadNum)
            pool.map(qiangQuanThread, [coupon for _ in range(threadNum)])
            pool.close()
            pool.join()
            print('等待下一波抢券!')


if __name__ == '__main__':
    # 每个任务启动一个进程
    # 当到达预设的开始时间，启动 threadNum 个线程，开始抢券，间隔时间 0.1
    # 当到达预设的结束时间，结束当前线程
    with Pool(len(coupons)) as p:
        p.map(qiangQuan, coupons)
