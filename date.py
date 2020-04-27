# -*- coding: utf-8 -*-

"""
@Time        : 2020/4/24
@Author      : dreamhomes
@File        : date
@Description : 获取日期
"""
import datetime
import sxtwl


def get_date():
    """
    Get date: solar + lunar calendar
    :return: String calendar
    """
    ymc = [u"十一", u"十二", u"正", u"二", u"三", u"四",
           u"五", u"六", u"七", u"八", u"九", u"十"]

    rmc = [u"初一", u"初二", u"初三", u"初四", u"初五", u"初六", u"初七", u"初八", u"初九", u"初十",
           u"十一", u"十二", u"十三", u"十四", u"十五", u"十六", u"十七", u"十八", u"十九", u"二十",
           u"廿一", u"廿二", u"廿三", u"廿四", u"廿五", u"廿六", u"廿七", u"廿八", u"廿九", u"三十", u"卅一"]

    numCn = ["天", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]

    # 获取阳历和阴历
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    lunar = sxtwl.Lunar()
    date_lunar = lunar.getDayBySolar(year, month, day)

    print_date = str(date_lunar.y) + "年" + str(date_lunar.m) + \
        "月" + str(date_lunar.d) + "日"

    if date_lunar.Lleap:
        print_lunar = "润" + ymc[date_lunar.Lmc] + \
            "月" + rmc[date_lunar.Ldi] + "日"
    else:
        print_lunar = ymc[date_lunar.Lmc] + "月" + rmc[date_lunar.Ldi] + "日"

    print_week = "星期" + numCn[date_lunar.week]

    calendar = print_date + ', ' + print_week + '\n' + \
        '农历' + print_lunar + '\n'

    return calendar
