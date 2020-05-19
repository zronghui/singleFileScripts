#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gooey import Gooey, GooeyParser


@Gooey()
def main():
    parser = GooeyParser(description='把想卖的基金金额转换成想卖的份额')

    parser.add_argument(
        'money',
        metavar='持有金额',
        help='')
    parser.add_argument(
        'share',
        metavar='持有份额',
        help='')
    parser.add_argument(
        'moneyToSell',
        metavar='今日想卖的金额',
        help='')

    args = parser.parse_args()
    print(args)
    print('应该卖出的份额: ', calculate(args.money, args.share, args.moneyToSell))


def calculate(money, share, moneyToSell):
    money, share, moneyToSell = float(money), float(share), eval(moneyToSell)
    return int(moneyToSell * share / money)


if __name__ == '__main__':
    main()
