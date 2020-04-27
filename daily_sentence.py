# -*- coding: utf-8 -*-

"""
@Time        : 2020/4/24
@Author      : dreamhomes
@File        : daily_sentence
@Description : 每日壹句-每日英语 / 每日情话
"""
import requests
import json


def get_daily_sentence():
    """
    Get  AiCiBa Daily Sentence
    return: string English + Chinese
    """
    url = 'http://open.iciba.com/dsapi/'
    r = requests.get(url)
    text = json.loads(r.text)
    english = text['content']
    chinese = text['note']
    daily_sentence = '\n@每日壹句:' + '\n' + english + '\n' + chinese + '\n'
    return daily_sentence


def get_daily_love():
    """
    每日情话
    :return: string
    """
    url = "https://api.lovelive.tools/api/SweetNothings/Serialization/Json"
    r = requests.get(url)
    all_dict = json.loads(r.text)
    sentence = all_dict['returnObj'][0]
    daily_love = '\n@每日情话:' + '\n' + sentence + '\n'
    return daily_love
