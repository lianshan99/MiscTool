# coding: gbk
import loginlibrary
import requests
import json
import time

token = loginlibrary.LoginLibrary().gettoken('13631276795', '123456')
uid = loginlibrary.LoginLibrary().getuid('13631276795', '123456')


def reportlocation():
    url = 'http://api.klgwl.com/user/location'
    params = {'type': 'gps', 'lat': '116.32715863448607', 'lng': '39.990912172420714', 'province': '北京', 'city': '北京',
              'town': '东直门', 'street': '大川胡同', 'street_number': '30'}
    params = loginlibrary.LoginLibrary().addsomeparams(params, '13631276795', '123456')
    r = requests.post(url, params=params)
    result = r.json()
    if result['result'] != 1:
        print(result)


def addactive():
    url = 'http://service.klgwl.com/activity/register'
    params = {'uid': uid, 'token': token, 'rid': '71414', 'start_time': '120', 'type': '0', 'lang': '1',
              "allow_range": '0', 'reward': '500', 'copy_num': '0'}
    params = loginlibrary.LoginLibrary().addsomeparamsMD5(params)
    r = requests.post(url, params=params)
    result = r.json()
    if result['code'] != 200:
        print(result)


reportlocation()
addactive()
