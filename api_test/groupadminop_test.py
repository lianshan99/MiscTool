# -*- coding:utf-8 -*-
import unittest
import requests
import time
import loginlibrary

user = '13631241428'
pwd = '123456'


class GroupAdminOPTest(unittest.TestCase):
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

    def test_group_admin_op(self):
        # 踢人出群
        url = '/group/kick'
        params = {}
        params = loginlibrary.LoginLibrary().addsomeparams(params, user, pwd)
        r = requests.post(url, params=params)
        result = r.json()
        self.assertEqual(result['result'], 1)

        # 修改群昵称


        # 修改群头像


        # 添加群公告


        # 编辑群公告


        # 查看群公告


        # 群禁言

        # 设置群成员禁言






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