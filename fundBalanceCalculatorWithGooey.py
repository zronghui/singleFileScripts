#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gooey import Gooey, GooeyParser


@Gooey()
def main():
    parser = GooeyParser(description='卖出一部分基金后计算基金余额')

    parser.add_argument(
        'money',
        metavar='持有金额',
        help='')
    parser.add_argument(
        'share',
        metavar='持有份额',
        help='')
    parser.add_argument(
        'selledShare',
        metavar='今日卖出份额',
        help='如果卖出多笔，可以使用 +')

    args = parser.parse_args()
    print(args)
    print('剩余金额: ', calculate(args.money, args.share, args.selledShare))


def calculate(money, share, selledShare):
    money, share, selledShare = float(money), float(share), eval(selledShare)
    return round(money / share * (share - selledShare), 1)


if __name__ == '__main__':
    main()
