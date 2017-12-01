# coding: gbk
import unittest
import requests
import time
import Rsa
import Passport
import loginlibrary

user = '13631241428'
pwd = '123456'


class DiscussPublicTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://api.klgwl.com/discuss/public'
        self.logincase = loginlibrary.LoginLibrary()
        self.token = self.logincase.gettoken(user,pwd)
        self.uid = self.logincase.getuid(user, pwd)
        self.params = {"lang": "1", "tags": "1", "media_type": "1", "is_top": "0", "content": "lianshan test",
                       "open_location": "0", "scan_type": "1", "allow_download": "1", "token": self.token,
                       "uid": self.uid}

    def test_discuss_public_onlytest_success(self):
        params_sign = self.params
        params_sign = self.logincase.addsign(params_sign)
        print(params_sign)
        r = requests.post(url=self.url, params=params_sign)
        print(r)
        # result = r.json()
        # self.assertEqual(result['result'], 1)

        # def tearDown(self):


if __name__ == '__main__':
    unittest.main()
