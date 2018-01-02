# coding: gbk
import loginlibrary
import requests
import json
import time

user = '13631276795'
pwd = '123456'

token = loginlibrary.LoginLibrary().gettoken(user, pwd)
uid = loginlibrary.LoginLibrary().getuid(user, pwd)


def reportlocationSZ():
    url = 'http://api.klgwl.com/user/location'
    params = {'type': 'gps', 'lat': '113.954161', 'lng': '22.542432', 'province': '北京', 'city': '北京',
              'town': '东直门', 'street': '大川胡同', 'street_number': '30'}
    params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
    r = requests.post(url, params=params)
    result = r.json()
    if result['result'] != 1:
        print(result)


def reportlocationBJ():
    url = 'http://api.klgwl.com/user/location'
    params = {'type': 'gps', 'lat': '116.32715863448607', 'lng': '39.990912172420714', 'province': '北京', 'city': '北京',
              'town': '东直门', 'street': '大川胡同', 'street_number': '30'}
    params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
    r = requests.post(url, params=params)
    result = r.json()
    if result['result'] != 1:
        print(result)


def addactive(type):  # 1 = 红包雨, 2 = 知识问答， 3 = 官方红包雨， 4 = 官方知识问答
    url = 'http://service.klgwl.com/activity/register'
    if type == 1:
        params = {'uid': uid, 'token': token, 'rid': uid, 'start_time': '10', 'type': '0', 'lang': '1',
                  "allow_range": '1', 'reward': '0', 'copy_num': '0'}

    elif type == 2:
        params = {'uid': uid, 'token': token, 'rid': uid, 'start_time': '10', 'type': '1', 'lang': '1',
                  "allow_range": '1', 'reward': '0', 'copy_num': '0', 'subtype': '1'}

    elif type == 3:
        params = {'uid': uid, 'token': token, 'rid': '71414', 'start_time': '120', 'type': '0', 'lang': '1',
                  "allow_range": '1', 'reward': '0', 'copy_num': '0', 'is_top': '1'}

    elif type == 4:
        params = {'uid': uid, 'token': token, 'rid': '71414', 'start_time': '300', 'type': '1', 'lang': '1',
                  "allow_range": '1', 'reward': '0', 'copy_num': '0', 'is_top': '1', 'subtype': '1'}

    params = loginlibrary.LoginLibrary().addsomeparamsMD5(params)
    r = requests.post(url, params=params)
    result = r.json()
    if result['code'] != 200:
        print(result)


# reportlocationBJ()
# reportlocationSZ()

addactive(4)  # 1 = 红包雨, 2 = 知识问答， 3 = 官方红包雨， 4 = 官方知识问答
