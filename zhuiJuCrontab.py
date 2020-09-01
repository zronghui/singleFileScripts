#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
为了不浪费腾讯视频 VIP，生成追剧的 crontab，到点自己打开网页
'''

name = input('剧名:')
url = input('网址:')
days = input('周几播放(如 1,4 表示周一和周四;0,6 表示周日周六; 1-5 表示周一至周五):')
hour = input('更新小时:')
minute = input('更新分钟:')
print(
f'''
# {name}
{minute} {hour} * * {days} open '{url}' > /dev/null 2>&1
'''
)