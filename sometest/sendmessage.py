import loginlibrary
import requests
import json
import time

token1 = loginlibrary.LoginLibrary().gettoken('13631241428', '123456')
token2 = loginlibrary.LoginLibrary().gettoken('13631231429', '123456')
token3 = loginlibrary.LoginLibrary().gettoken('13631276795', '123456')
url = 'http://api.klgwl.com/message/send'


def sendmsg(i):
    # uid = loginlibrary.LoginLibrary().getuid('13631241428', '123456')
    params = {'uid': '63389', 'token': token1, 'to': '10790', 'msg': i, 'type': '1'}
    params = loginlibrary.LoginLibrary().addsign(params)
    requests.post(url, params=params)


def Bsendmsg(i):
    # uid = loginlibrary.LoginLibrary().getuid('13631231429', '123456')
    params = {'uid': '63388', 'token': token2, 'to': '10790', 'msg': i, 'type': '1'}
    params = loginlibrary.LoginLibrary().addsign(params)
    requests.post(url, params=params)


def Csendmsg(i):
    # uid = loginlibrary.LoginLibrary().getuid('13631276795', '123456')
    params = {'uid': '71414', 'token': token3, 'to': '10790', 'msg': i, 'type': '1'}
    params = loginlibrary.LoginLibrary().addsign(params)
    requests.post(url, params=params)


for i in range(10):
    print(i)
    sendmsg(i + 1)
    Bsendmsg(i + 1)
    Csendmsg(i + 1)
