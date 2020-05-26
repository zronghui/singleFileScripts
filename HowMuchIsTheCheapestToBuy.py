#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gooey import Gooey, GooeyParser
from tabulate import tabulate

thingPriceDict = {
    # 吃
    '吃--娃哈哈 ad 钙奶': '41 / 24*220g',
    '吃--蒙牛纯牛奶': '1.625 / 瓶',
    '吃--伊利无乳糖高钙': '1.86 / 瓶',
    '吃--纯甄芒果味': '2.17 / 瓶',
    '吃--纯甄原味': '1.93 / 瓶',
    '吃--芝士乳酸菌蒸蛋糕': '2 / 100g',
    '吃--阿尔卑斯软糖': '20 / 斤',
    '吃--米多奇馍丁': '7 / 10包',
    # '': ' / ',
    # 用
    '用--蚊香': '0.19 / 单盘',
    '用--力士沐浴露': '2.96 / 100g',
    '用--心相印抽纸': '1 / 120抽',
    '用--小米5/7号电池': '1 / 节',
    '用--苍蝇纸': '0.2 / 张',
    '用--保鲜膜': '2.31 / 100 米',
    '用--TPU键盘膜': '12.8 / 张',
    '用--云南白药套装': '14 / 100g',
    '用--立白洗衣液': '5.625 / KG',
    '用--暖水瓶': '28 / 个',
    '用--小号挂钩': '1 / 3个',
    '用--得力 A4 纸': '19 / 500张',
    '用--清扬 650 g': '35',
    '用--立白洗洁精': '7.59 / kg',
    '用--舒肤佳香皂': '4.33 / 块',
    '用--格力 1.5 匹': '2000 / 台',
    '用--33cm 对折拖把': '42 / 个',
    '用--3M n95': '4 / 个',
    # '': ' / ',
    # 穿
    '穿--南极人内裤': '12.5 / 条',
    '穿--南极人袜子': '3 / 双',
    '穿--爱马斯一次性口罩': '0.24 / 个',
    # '': ' / ',
}


@Gooey()
def main():
    parser = GooeyParser(description='计算买多少最便宜')

    parser.add_argument(
        'numAndPrice',
        metavar='数目/重量:价格--',
        help='')
    parser.add_argument(
        '-t',
        '--thing',
        metavar='买的什么东西',
        choices=thingPriceDict.keys(),
        help='提供一个我买到的最低价'
    )

    args = parser.parse_args()
    print(args)
    print('我买的最低单价: ', thingPriceDict.get(args.thing))
    sortAndPrint(args.numAndPrice)


def sortAndPrint(numAndPrice):
    table = [
        [
            float(eval(i.split(':')[0].strip())),
            float(eval(i.split(':')[1].strip())),
        ]
        for i in numAndPrice.split('--')
    ]
    for i in table:
        i.append(round(i[1] / i[0], 2))
    table.sort(key=lambda i: i[2])
    table.insert(0, ['数目/重量', '价格', '单价'])
    print(tabulate(table))


if __name__ == '__main__':
    main()
