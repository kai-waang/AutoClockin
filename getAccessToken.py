# -*- coding: utf-8 -*-

import requests
import time
import pickle
import os

path = './token.pickle'
ak = '【官网获取的AK】'
sk = '【官网获取的SK】'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(ak,
                                                                                                                     sk)


def getToken():  # 请求获取token
    r = requests.get(host)
    if r:
        return r.json()['access_token']


def saveToken(token):  # 保存获取的token
    with open(path, 'wb') as f:
        pickle.dump(token, f)


def resetToken():  # 重置本地token
    access_token = dict()
    access_token['time'] = str(time.time())
    access_token['token'] = getToken()
    saveToken(access_token)
    return access_token


def getAccessToken():
    if os.path.exists(path):
        with open(path, 'rb') as f:
            try:
                access_token = pickle.load(f)
                if time.time() - eval(access_token['time']) > 2626560:  # 本地token已过期则重新获取并更新
                    print('access token已过期，正在重新获取')
                    return resetToken()['token']
                else:
                    return access_token['token']  # 使用本地token

            except EOFError:  # 本地token若为空，则获取、存储后返回
                print('未找到token，正在获取')
                return resetToken()['token']
    else:  # 本地token不存在
        return resetToken()['token']

