# coding: gbk
import unittest
import requests
import time
import Rsa
import Passport
import loginlibrary

user = '13631241428'
pwd = '123456'


class ReplyTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://api.klgwl.com/social/reply'

    def test_add_reply(self):  # 添加回复
        content = str(time.time()).split('.')[0]
        params = {'type': 'discuss', 'comment_id': '2236', 'content': content}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        r = requests.post(self.url, params=params)
        result = r.json()
        self.assertEqual(result['result'], 1)

    def tearDown(self):
        # 获取评论列表，得到评论id
        url = 'http://api.klgwl.com/social/commentList'
        params = {"type": "discuss", "item_id": "34500"}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        r = requests.post(url, params=params)
        result = r.json()
        print(result)
        self.assertEqual(result['result'], 1)
        item_id = result['data']['data_list'][0]['comment_id']
        # 删除评论
        url = 'http://api.klgwl.com/social/removeComment'
        params = {"type": "comment", "item_id": item_id}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        r = requests.post(url, params=params)
        result = r.json()
        self.assertEqual(result['result'], 1)


if __name__ == '__main__':
    unittest.main()
