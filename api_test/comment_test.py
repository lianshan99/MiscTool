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
        self.url = 'http://api.klgwl.com/social/comment'
        self.item_id = ''

    def test_add_comment(self):
        content = str(time.time()).split('.')[0]
        params = {"type": "discuss", "item_id": "34500", "content": content}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        print(params)
        r = requests.post(self.url, params=params)
        print(r.content.decode())
        result = r.json()
        self.assertEqual(result['result'], 1)

    def test_get_commentlist(self):
        url = 'http://api.klgwl.com/social/commentList'
        params = {"type": "discuss", "item_id": "34500"}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        print(params)
        r = requests.post(url, params=params)
        print(r.content.decode())
        result = r.json()
        self.assertEqual(result['result'], 1)


if __name__ == '__main__':
    unittest.main()
