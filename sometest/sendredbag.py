# coding: gbk
import loginlibrary
import requests
import json
import time

token1 = loginlibrary.LoginLibrary().gettoken('13631241428', '123456')
token2 = loginlibrary.LoginLibrary().gettoken('13631231429', '123456')
# token3 = loginlibrary.LoginLibrary().gettoken('13631276795', '123456')
url = 'http://api.klgwl.com/redbag/newbag'


def asendredbag(i):
    params = {'uid': '63389', 'token': token1, 'to_uid': '63388', 'num': 1, 'money': '1', 'content': i, 'random': 1,
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
    params = {'uid': '63388', 'token': token2, 'to_uid': '63389', 'num': 1, 'money': '1', 'content': i, 'random': 1,
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


for i in range(1):
    print(i)
    #个人私发红包
    asendredbag(i + 1)
    bsendredbag(i + 1)

    #群红包
    # asendredbagtogroup(i + 1)
    # bsendredbagtogroup(i + 1)
