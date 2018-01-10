# coding: gbk
import loginlibrary
import requests
import json
import time

data1 = loginlibrary.LoginLibrary().getlogin('13631241428', '123456')
token1 = data1.get('token')
uid1 = data1.get('uid')
data2 = loginlibrary.LoginLibrary().getlogin('13631231429', '123456')
token2 = data1.get('token')
uid2 = data1.get('uid')
url = 'http://api.klgwl.com/redbag/newbag'


def asendredbag(i):
    params = {'uid': uid1, 'token': token1, 'to_uid': '63388', 'num': 1, 'money': '1', 'content': i, 'random': 1,
              'from': '0'}
    params = loginlibrary.LoginLibrary().addsomeparamsMD5(params)
    r = requests.post(url, params=params)
    result = r.json()
    if result['code'] != 0:
        print(result)
    else:
        redid = result['data']
        url1 = 'http://api.klgwl.com/redbag/grabbag'
        params1 = {'uid': '63388', 'redid': redid, 'e_type': 'MD5'}
        params1 = loginlibrary.LoginLibrary().addsomeparamsMD5(params1)
        requests.post(url1, params=params1)


def bsendredbag(i):
    # uid = loginlibrary.LoginLibrary().getuid('13631231429', '123456')
    params = {'uid': uid2, 'token': token2, 'to_uid': '63389', 'num': 1, 'money': '1', 'content': i, 'random': 1,
              'from': '0'}
    params = loginlibrary.LoginLibrary().addsomeparamsMD5(params)
    r = requests.post(url, params=params)
    result = r.json()
    if result['code'] != 0:
        print(result)
    else:
        redid = result['data']
        url1 = 'http://api.klgwl.com/redbag/grabbag'
        params1 = {'uid': '63389', 'redid': redid, 'e_type': 'MD5'}
        params1 = loginlibrary.LoginLibrary().addsomeparamsMD5(params1)
        requests.post(url1, params=params1)


def bsendredbagtogroup(i):
    params = {'uid': '63388', 'token': token2, 'to_gid': '158238559', 'num': 1, 'money': '1', 'content': i, 'random': 1,
              'from': '0'}
    params = loginlibrary.LoginLibrary().addsomeparamsMD5(params)
    r = requests.post(url, params=params)
    result = r.json()
    if result['code'] != 0:
        print(result)
    else:
        redid = result['data']
        url1 = 'http://api.klgwl.com/redbag/grabbag'
        params1 = {'uid': '63388', 'redid': redid, 'e_type': 'MD5'}
        params1 = loginlibrary.LoginLibrary().addsomeparamsMD5(params1)
        requests.post(url1, params=params1)


def asendredbagtogroup(i):
    params = {'uid': '63389', 'token': token1, 'to_gid': '158238559', 'num': 1, 'money': '1', 'content': i, 'random': 1,
              'from': '0'}
    params = loginlibrary.LoginLibrary().addsomeparamsMD5(params)
    r = requests.post(url, params=params)
    result = r.json()
    if result['code'] != 0:
        print(result)
    else:
        redid = result['data']
        url1 = 'http://api.klgwl.com/redbag/grabbag'
        params1 = {'uid': '63389', 'redid': redid, 'e_type': 'MD5'}
        params1 = loginlibrary.LoginLibrary().addsomeparamsMD5(params1)
        requests.post(url1, params=params1)


for i in range(10):
    print(i)
    #个人私发红包
    # asendredbag(i + 1)
    # bsendredbag(i + 1)

    #群红包
    asendredbagtogroup(i + 1)
    bsendredbagtogroup(i + 1)
