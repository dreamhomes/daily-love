# -*- coding: utf-8 -*-

"""
@Time       : 2020/4/20 9:49
@Author     : dreamhomes
@File       : DailyWarning.py
@Description: 每日温暖提醒实现： @日期/农历 + @每日壹句/每日情话 + @天气预报 + @天气指数
"""
import argparse
import schedule
import time
import datetime
import itchat

from daily_sentence import *
from date import get_date
from china_weather import get_information

# 若出现二维码显示错误则令 enableCmdQR=2
itchat.auto_login(hotReload=True, enableCmdQR=True)

parser = argparse.ArgumentParser(description="*** Input parameters ***")
parser.add_argument('-s', '--sender', type=str, help='Sender')
parser.add_argument('-r', '--recipient', type=str, help='recipient')
parser.add_argument('-c', '--city', default="101240214", type=str, help='city code')
parser.add_argument('-t', '--time', default="8:00", type=str, help='reminder time')
args = parser.parse_args()
# print(args.sender, args.recipient, args.city, args.time)

xxx = "来自 @"+args.sender+" 的爱，么么哒：\n\n"
location = "http://www.weather.com.cn/weather/" + args.city + ".shtml"

name = itchat.search_friends(nickName=args.recipient)[0]['UserName']


def main():
    message = xxx + get_date() + get_daily_love() + get_information(location)
    print('The message sending time:', datetime.datetime.now())
    print(message)
    # test
    # itchat.send_msg(msg=message, toUserName='filehelper')
    itchat.send_msg(msg=message, toUserName=name)


# schedule.every(60).seconds.do(main)
schedule.every().day.at(args.time).do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
