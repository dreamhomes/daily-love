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
import threading

from daily_sentence import *
from date import get_date
from china_weather import get_information

# 若出现二维码显示错误则令 enableCmdQR=2
itchat.auto_login(hotReload=True, enableCmdQR=True)

parser = argparse.ArgumentParser(description="*** Input parameters ***")
parser.add_argument('-s', '--sender', type=str, help='Sender')
parser.add_argument('-r', '--recipient', type=str, help='recipient')
parser.add_argument('-c', '--city', default="101240214", type=str, help='city code')
parser.add_argument('-t', '--time', default="08:00", type=str, help='reminder time')
args = parser.parse_args()
print(args.sender, args.recipient, args.city, args.time)

begin = "亲爱的 @琪琪宝贝：\n\n"
end = "\n\n来自 @"+args.sender+" 的爱，么么哒！"
location = "http://www.weather.com.cn/weather/" + args.city + ".shtml"

name = itchat.search_friends(nickName=args.recipient)[0]['UserName']


def main():
    message = begin + get_date() + get_daily_love() + get_information(location) + end
    print('The message sending time:', datetime.datetime.now())
    print(message)
    # test
    # itchat.send_msg(msg=message, toUserName='filehelper')
    itchat.send_msg(msg=message, toUserName=name)


def hold():
    """
    hold wechat sign in.
    :return:
    """
    itchat.send_msg(msg="", toUserName='filehelper')


def threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every().hour.do(threaded, hold)
schedule.every().day.at(args.time).do(threaded, main)
while True:
    schedule.run_pending()
    time.sleep(1)
