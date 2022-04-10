# encoding=utf-8
import json
import unittest
import warnings

from ddt import ddt, data

from test_case.login import *
from tool.do_excel import GetExcel
from tool.my_log import Mylog
from tool.project_path import *

# 获取excel中数据
test_data2 = GetExcel(testcase_path, 'find').get_data()

mylog = Mylog()
@ddt()
class Find(unittest.TestCase):
    @data(*test_data2)
    def test_find(self, item):
        # 从文件中获取最新得token值
        file = open(r"E:\pycharm\code\ningmeng\API_AUTO\test_case\access_token.txt", "r", encoding='utf-8')
        a_token = file.read()
        print("打印出来这个token值".format(a_token))
        header = {"X-Authorization-access_token": a_token}
        # 从excel中取出得是字符串，转化成字典格式需要
        res = Http_Request().http_request(item['method'], item['url'], eval(item['data']), header)
        warnings.simplefilter("ignore", ResourceWarning)
        print("查询合同的结果是：", res.json())
        try:
            self.assertEqual(200, res.json()['state'])
            test_result = "测试通过"
        except Exception as e:
            mylog.error("这里出现异常了".format(e))
            test_result = "测试不通过"
        finally:
            GetExcel(testcase_path, 'find').data_write(item['case']+1,test_result, str(res.json()))


if __name__ == '__main__':
    unittest.main()
