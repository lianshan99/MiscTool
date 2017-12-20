# coding: gbk
import time
import requests
import Rsa
import Passport

localtime = str(time.time())
timpstamp = localtime.split('.')[0]


class LoginLibrary():
    def reqpost(self, api, params):
        url = "http://api.klgwl.com" + api  # 测试的接口url
        r = requests.post(url=url, params=params)
        return r.json()

    def getlogin(self, user, pwd):
        login_params = {'phone': user, 'pwd': Rsa.Verify().publicSign(pwd), 'os_version': '4.2', 'phone_model': '荣耀6',
                        'device_id': 'tester', 'welcome': '0'}
        login_params = self.addsign(login_params)
        result = self.reqpost('/user/login', login_params)
        return result

    def addsign(self, params):
        params['time_stamp'] = str(time.time()).split('.')[0]
        params['client_type'] = 'android'
        params['app_version'] = '2.2.3204'
        params['sign'] = Passport.Identify().buildRequestMysign(params, 'RSA')
        return params

    def addsomeparams(self, params, user, pwd):
        params['token'] = self.gettoken(user, pwd)
        params['uid'] = self.getuid(user, pwd)
        params['time_stamp'] = str(time.time()).split('.')[0]
        params['client_type'] = 'android'
        params['app_version'] = '2.2.3204'
        params['sign'] = Passport.Identify().buildRequestMysign(params, 'RSA')
        return params

    def addsomeparamsMD5(self, params):
        params['time_stamp'] = str(time.time()).split('.')[0]
        params['client_type'] = 'android'
        params['app_version'] = '2.2.3204'
        params['sign'] = Passport.Identify().buildRequestMysign(params, 'MD5')
        params['sign_type'] = 'MD5'
        return params

    def gettoken(self, user, pwd):
        result = self.getlogin(user, pwd)
        token = result['data']['token_info']['token']
        return token

    def getuid(self, user, pwd):
        result = self.getlogin(user, pwd)
        uid = result['data']['uid']
        return uid
