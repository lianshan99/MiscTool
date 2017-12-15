# coding: gbk
import unittest
import requests
import time
import Rsa
import Passport

localtime = str(time.time())
timpstamp = localtime.split('.')[0]
user = '13631241428'
pwd = '123456'

class UserLoginTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://api.klgwl.com/user/login'
        self.params = {'phone': user, 'pwd': Rsa.Verify().publicSign(pwd), 'os_version': '4.2', 'phone_model': '荣耀6',
              'device_id': 'tester', 'welcome': '0', 'time_stamp': timpstamp, 'client_type': 'android',
              'app_version': '2.2.3003'}

    def test_user_login_success(self):
        params_sign = self.params
        params_sign['sign'] = Passport.Identify().buildRequestMysign(params_sign, 'RSA')
        r = requests.get(self.url, params=params_sign)
        result = r.json()
        self.assertEqual(result['result'], 1)

    # def tearDown(self):


if __name__ == '__main__':
    unittest.main()
