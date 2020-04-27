# -*- coding: utf-8 -*-

"""
@Time        : 2020/4/24
@Author      : dreamhomes
@File        : china_weather
@Description : 获取中国天气网信息
"""
import requests
import re


def get_information(html):
    """
    Get More Weather Information.
    Arguments:
        html {String} -- location html

    Returns:
        String -- Information
    """
    response = requests.get(html)
    content = response.content.decode("utf-8")
    aim = re.findall(
        r'<input type="hidden" id="hidden_title" value="(.*?)月(.*?)日(.*?)时(.*?) (.*?)  (.*?)  (.*?)"',
        content)
    air_data = re.findall(
        r'<li class="li6">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>',
        content)
    ult_index = re.findall(
        r'<li class="li1">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>',
        content)
    cloth_index = re.findall(
        r'<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</a>\n</li>\n<li class="li4">',
        content)
    # wash_index = re.findall(r'<li class="li4">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>', content)
    lose_index = re.findall(
        r'</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</a>\n</li>\n<li class="li5">',
        content)
    # print(lose_index)
    txt1 = '@每日提醒:' + '\n'
    txt2 = '天气情况: ' + aim[0][5] + '\n' + '温度情况: ' + aim[0][6] + '\n'
    txt3 = '穿衣指数: ' + cloth_index[0][0] + ', ' + cloth_index[0][2] + '\n'
    txt4 = '减肥指数：' + lose_index[0][1] + '\n'
    txt5 = '空气指数: ' + air_data[0][0] + ', ' + air_data[0][2] + '\n'
    txt6 = '紫外线指数: ' + ult_index[0][0] + ', ' + ult_index[0][2] + '\n'

    # txt7 = '洗车指数: '+wash_index[0][0]+', '+wash_index[0][2]+'\n'

    more_information = '\n' + txt1 + txt2 + txt3 + txt4 + txt5 + txt6
    return more_information

