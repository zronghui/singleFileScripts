# singleFileScripts
自己写的一些单文件脚本



依赖安装

```shell
pip3 install -r requirements.txt
```

## 北邮

### buptBathReserve.py

会自动检查 cookie 和失败重试，cookie 失效或者抢到 之后会发送邮件通知

```shell
*/10 * * * * cd /root/code/singleFileScripts && $python buptBathReserve.py
```



## 京东

### jdQiangQuan.py

-- 京东抢券 多进程+多线程

1. 浏览器试着点击领取优惠券，copy as curl
2. pbpaste | sed 's/curl/curl -s/g' > jd1.sh # -s : silence
3. vim jdQiangQuan.py 设置以下内容

```python
threadNum = 8  # 抢券线程数
interval = 0.1  # 失败重试间隔
secondsAhead = 1  # 提前几秒开始抢券
# 目前只支持整点抢券
coupons = [
    {
        'name': '伊利199-100', # 9月1 - 30日
        'time': '0/10/16/20',
        'command': './jd1.sh',
        'couponUrl': ''
    }
]
```

可能 curl 执行失败，因为 curl 版本低，需要将 data-raw 替换为 data

```shell
grep -rl 'data-raw' . | xargs -I _ sed -i 's/data-raw/data/g' _
```





[京东触屏版](https://home.m.jd.com/myJd/newhome.action)
[开学“鲜”行站](https://prodev.m.jd.com/mall/active/2NZH88vEYUjzQra71PbGChxZXrbi/index.html?_ts=1597369967804&utm_user=plusmember&gx=RnFjl2UPaTOKmtRP--twX2Qj-Q8Km8Ot_nwh&ad_od=share&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL#/)
[818手机节](http://jd.cn.hn/ajSz)
[伊利 199-100](http://jd.cn.hn/ajS2)



TODO：筛选出同时符合多个优惠的商品，如同时能用 5 折 + 49-20 优惠券

## 基金相关
### fundBalanceCalculatorWithGooey.py

-- 卖出一部分基金后计算基金余额

### howMuchShareShouldISell.py

-- 把想卖的基金金额转换成想卖的份额



## 其他

### pbcopy

-- 类似于 Mac 的 pbcopy, 服务器拷贝到剪贴板

### HowMuchIsTheCheapestToBuy.py

-- 计算买多少最便宜

### zhuiJuCrontab.py

为了追剧，到更新时间自动打开更新页面，生成类似于↓的 crontab 配置

```shell
# 一念永恒
55 9 * * 3 open 'https://v.qq.com/detail/w/ww18u675tfmhas6.html' > /dev/null 2>&1
```



