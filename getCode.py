# -*- coding: utf-8 -*-

import requests
import json
import base64
from getAccessToken import getAccessToken

token = ''


def get_token():  # 获取验证码的token
    global token
    r = requests.get("https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode")
    token = json.loads(r.text)["data"]["Token"]
    return token


def get_img(tk):  # 获取与token对应的验证码图片
    r = requests.get("https://fangkong.hnu.edu.cn/imagevcode?token=" + tk)
    return r.content


def get_code():  # 识别验证码
    img = get_img(get_token())
    im = base64.b64encode(img)  # base64编码
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    params = {"image": im}
    access_token = getAccessToken()  # 获取调用API所需的access_token
    request_url = request_url + "?access_token=" + access_token  # 构造请求URL
    headers = {'content-type': 'application/x-www-form-urlencoded'}  # 请求头
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        res = dict()
        res['code'] = response.json()['words_result'][0]['words']
        res['token'] = token
        return res  # 返回结果，包含验证码和对应的token
