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
        self.url = 'http://api.klgwl.com/discuss/publish'
        self.discuss_id = ''

    def test_discuss_public_onlytest_success(self):
        content = 'lianshan test' + str(time.time()).split('.')[0]
        params = {"lang": "1", "tags": "1", "media_type": "1", "is_top": "0", "content": content,
                  "open_location": "0", "scan_type": "1", "allow_download": "1"}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        print(params)
        r = requests.post(self.url, params=params)
        print(r.content.decode())
        result = r.json()
        self.assertEqual(result['result'], 1)
        self.discuss_id = result['data']

    def tearDown(self):
        params = {"discuss_id": self.discuss_id}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        print(params)
        r = requests.post('http://api.klgwl.com/discuss/delete', params=params)
        print(r.content.decode())
        result = r.json()
        self.assertEqual(result['result'], 1)


if __name__ == '__main__':
    unittest.main()
