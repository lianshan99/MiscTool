# -*- coding:utf-8 -*-
import unittest
import requests
import time
import loginlibrary

user = '13631241428'
pwd = '123456'


class GroupOPTest(unittest.TestCase):
    def setUp(self):
        # new group and get the gid
        url = 'http://api.klgwl.com/group/add'
        params = {'to_uid': '63362,63499', 'avatar': 'http://avatorimg.klgwl.com/151262611034470_s_1020x900.jpg'}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        r = requests.post(url, params=params)
        result = r.json()
        self.assertEqual(result['result'], 1)
        self.gid = result['data']['gid']
        print(self.gid)

    def test_group_op(self):
        # A join the group
        url = 'http://api.klgwl.com/group/join'
        params = {'gid': self.gid, 'avatar': 'http://avatorimg.klgwl.com/151262611034470_s_1020x900.jpg',
                  'invitor': '63389', }
        params = loginlibrary.LoginLibrary().addsomeparams(params, '13631231429', '123456')
        r = requests.post(url, params=params)
        result = r.json()
        self.assertEqual(result['result'], 1)

        # kick A out of the group
        url = 'http://api.klgwl.com/group/kick'
        params = {'gid': self.gid, 'to_uid': '63388'}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        r = requests.post(url, params=params)
        result = r.json()
        self.assertEqual(result['result'], 1)

        # invite A to join the group
        url = 'http://api.klgwl.com/group/invite'
        params = {'invitor': '63389', 'gid': self.gid, 'to_uid': '63388'}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        r = requests.post(url, params=params)
        result = r.json()
        self.assertEqual(result['result'], 1)

    def tearDown(self):
        # 解散该群
        url = 'http://api.klgwl.com/group/dissolve'
        params = {'gid': self.gid}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        r = requests.post(url, params=params)
        result = r.json()
        self.assertEqual(result['result'], 1)


if __name__ == '__main__':
    unittest.main()
