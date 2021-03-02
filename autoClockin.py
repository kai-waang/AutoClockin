# -*- coding: utf-8 -*-

from getCode import get_code
from usrs import users
import requests

s = requests.session()
back_state = 1  # 返校状态


def post(usr):  # 登陆的post请求
    code = get_code()  # 获取验证码以及与之对应的token
    params = {  # 请求参数
        'Code': usr['code'],
        'Password': usr['passwd'],
        'Token': code['token'],
        'VerCode': code['code'],
    }
    request_url = 'https://fangkong.hnu.edu.cn/api/v1/account/login'
    return s.post(url=request_url, data=params)  # 请求登陆


def login(usr):
    global back_state
    r = post(usr).json()
    while r['code'] != 0:
        print("登陆失败-{},正在重试".format(r['msg']))
        r = post(usr).json()
    back_state = r['data']['BackState']
    if back_state:
        print("{0:{2}<5}{1}  登陆成功 [已返校]----".format(r['data']['Name'], r['data']['LoginTime'], chr(12288)), end='')
    else:
        print("{0:{2}<5}{1}  登陆成功 [未返校]----".format(r['data']['Name'], r['data']['LoginTime'], chr(12288)), end='')
    return r


def clock_in(usr):
    request_url = 'https://fangkong.hnu.edu.cn/api/v1/clockinlog/add'  # 请求URL
    params = [  # 请求参数
        {  # 未返校参数
            "Temperature": None,
            "RealProvince": usr['province'],
            "RealCity": usr['city'],
            "RealCounty": usr['county'],
            "RealAddress": usr['address'],
            "IsUnusual": "0",
            "UnusualInfo": "",
            "IsTouch": "0",
            "IsInsulated": "0",
            "IsSuspected": "0",
            "IsDiagnosis": "0",
            "tripinfolist": [{
                "aTripDate": "",
                "FromAdr": "",
                "ToAdr": "",
                "Number": "",
                "trippersoninfolist": []
            }],
            "toucherinfolist": [],
            "dailyinfo": {
                "IsVia": "0", "DateTrip": ""
            },
            "IsInCampus": "0",
            "IsViaHuBei": "0",
            "IsViaWuHan": "0",
            "InsulatedAddress": "",
            "TouchInfo": "",
            "IsNormalTemperature": "1",
            "Longitude": None,
            "Latitude": None
        },
        {  # 已返校参数
            "BackState": 1,
            "Latitude": None,
            "Longitude": None,
            "MorningTemp": "36.4",
            "NightTemp": "36.4",
            "RealAddress": "天马公寓",  # 按需要修改为其他
            "RealCity": "长沙市",
            "RealCounty": "岳麓区",
            "RealProvince": "湖南省",
            "tripinfolist": []
        }]

    r = s.post(url=request_url, json=params[int(back_state)])  # 打卡请求，参数根据在校状态选择
    print(r.json()['msg'])  # 打印结果
    return r


if __name__ == '__main__':
    for user in users:
        login(users[user])
        clock_in(users[user])
