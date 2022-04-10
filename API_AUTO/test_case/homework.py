# encoding=utf-8
"""
完成register、login、recharge接口的请求：
1、把自己的测试用例写到excel中
2、编写excel读取和存储测试数据的类，从excel中获取必要的测试数据
3、编写一个http请求完成注册、登录、充值接口的测试
4、创建实例完成接口测试，并同步把结果存到excel中
5、做好测试代码、测试数据、文件的分离

"""
from tool.do_excel import GetExcel
import unittest
from ddt import ddt, data  # 列表嵌套列表，列表嵌套字典都是可以用ddt脱掉外衣
import json
import warnings
# 获取到excel中的数据， excel中数据与配置文件中绑定，只读取配置文件选择的数据列
from tool.http_request import Http_Request
from tool.project_path import *
from tool.my_log import *

# 可以用绝对路径来读取文件，因为如果直接输入文件名是只在当前路径下获取
# 前面加r进行转译
test_data = GetExcel(testcase_path, 'login').get_data()

my_log = Mylog()


@ddt()  # 使用ddt获取数据
class Login(unittest.TestCase):
    @data(*test_data)  # 使用脱外衣的方式脱掉test_data外层的列表属性
    # 给获取的test_data数据全部赋值到item中去，遍历
    def test_login(self, item):
        print("这是请求的方式:{0}".format(item['method']))
        print("这是请求的地址:{0}".format(item['url']))
        print("这是请求的参数:{0}".format(item['data']))
        print("这是请求的期望值:{0}".format(item['expect']))
        # 第一种方法：因为从excel中读取的数据，数字是int格式，其他全是字符串，所以要将字符串转换为字典格式 因为该接口只支持字典格式
        # data = json.loads(item['data'])
        print(f"[正在测试的用例是]:{item['title']}")
        # 第二种方法：给数据eval 恢复成原本的数据类型
        """
        如果有参数化的请求，要用到上一个请求返回的数据，要在这里进行数据的替换，在请求之前完成
        """
        res = Http_Request().http_request(item['method'], item['url'], eval(item['data']))
        warnings.simplefilter("ignore", ResourceWarning)
        print(f"[这是请求返回的结果]:{res.json()}")
        try:
            # 如果没有异常，test_result里写入测试通过
            self.assertEqual(item['expect'], res.json()['state'])
            test_result = '测试通过'
        except Exception as e:
            file = open("test.txt", "w+", encoding="utf-8")
            file.write(str(e))
            # 如果有异常，test_result里写入测试不通过
            test_result = '测试不通过'
            my_log.info(f"[执行用例出错了]:{e}")
            raise e  # raise相当于return 后面代码就不执行了，但是finally无论怎么样后面代码都会执行
        # 调用GetExcel中的data_write方法，在case+1行每个里面写入返回结果
        # 这里有个容易出现错误的地方：json格式没办法写入excel 要转为字符串格式
        finally:  # 不管报不报异常结果不影响我 都要写进去
            GetExcel(testcase_path, 'login').data_write(item['case'] + 1, 8, test_result)
            GetExcel(testcase_path, 'login').data_write(item['case'] + 1, 9, str(res.json()))
        return res.text


if __name__ == '__main__':
    unittest.main()
