# coding: gbk
import time, sys
from HTMLTestRunner import HTMLTestRunner
import unittest


# ָ����������Ϊ��ǰ�ļ����µ� klg_api Ŀ¼
test_dir = './api_test'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='klgwl System Interface Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()