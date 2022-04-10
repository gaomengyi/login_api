"""
执行文件：执行代码的入口
"""

import unittest
import HTMLTestRunner

from test_case import find_ht
from test_case.find_ht import Find
from test_case.homework import *

"""
多个用例怎么同时执行？
1、写多个模块，不同的模块就用不同的模块名称去加载
2、用配置文件，在配置文件中修改就可以控制用例的加载
"""
suite = unittest.TestSuite()
loder = unittest.TestLoader()

suite.addTest(loder.loadTestsFromTestCase(Login))#加载LOgin类下面的用例
# suite.addTest(loder.loadTestsFromModule(find_ht))

# 执行文件
# report_path调用project_path设置的路径
with open(report_path, 'wb')as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='登录页面的测试', description='登录页面的详细报告',
                                           tester='gmm')
    runner.run(suite)
