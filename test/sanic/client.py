'''
测试客户端
'''
import unittest
from time import time
from test.httpie_utils import http
from test.httpietestbase import API_HOST

class Test(unittest.TestCase):
    '''
    基础测试
    '''
    def setUp(self):
        self.start = time()

    def tearDown(self):
        print(time() - self.start)
    
    def test_get_methods(self):
        '''
        测试get方法
        '''
        r = http('GET', '{host}/tag/{url}'.format(host=API_HOST, url='23'))
        # print(r.join)
        self.assertEqual(int(r.json['tag']), 23)

    def test_get_blue(self):
        '''
        测试蓝图
        '''
        r = http('GET', '{host}/{url}'.format(host=API_HOST, url='blue/root?key1=value1&key2=value2'))
        print(r)

    def test_get_view(self):
        '''
        测试view
        '''
        r = http('GET', '{host}/{url}'.format(host=API_HOST, url='blue/view'))
        print(r)

    def test_post_methods(self):
        '''
        post method
        '''
        r = http('POST', '{host}/name/{url}'.format(host=API_HOST, url='姓名'))
        print(r)

if __name__ == '__main__':
    unittest.main()