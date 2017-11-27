# coding: gbk
import unittest
import requests
import time
import Passport
import Rsa

localtime = time.time()
timpstamp = localtime.split('.')[0]
user = '13631241428'
pwd = '123456'


class UserLoginTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://api.klgwl.com/user/login'
        self.params = {'phone': user, 'pwd': Rsa.Verify().publicSign(pwd), 'os_version': '4.2', 'phone_model': '荣耀6',
              'device_id': 'tester', 'welcome': '0', 'time_stamp': timpstamp, 'client_type': 'android',
              'app_version': '2.2.3003'}

    # def test_user_login_phone_null(self):
    #     r = requests.get(self.url, params={'phone': ''})
    #     result = r.json()
    #     print(result)
    #     self.assertEqual(result['result'], 0)
    #     self.assertEqual(result['error']['msg'], "无效的签名")

    def test_user_login_success(self):
        r = requests.get(self.url, params=self.params)
        result = r.json()
        self.assertEqual(result['result'], 1)
    # def tearDown(self):


if __name__ == '__main__':
    unittest.main()
