# coding: gbk
import time
import requests
import Rsa
import Passport
import loginlibrary
import threading


def regist():
    url = 'http://120.78.182.253:8181/user/register'
    username = 'tester'
    phone = '18888888883'
    params = {'username': username, 'pwd': Rsa.Verify().publicSign('123456'), 'phone': phone, 'sex': '1', 'birthday': '20150302', 'code': '888888'}
    params = loginlibrary.LoginLibrary().addsign(params)
    r = requests.post(url, params=params)
    result = r.json()
    # if result['result'] != 1:
    #     print(result)
    print(result)


threads = []
t1 = threading.Thread(target=regist)
threads.append(t1)
t2 = threading.Thread(target=regist)
threads.append(t2)
t3 = threading.Thread(target=regist)
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        print(time.time())
        t.setDaemon(True)
        t.start()

    t.join()