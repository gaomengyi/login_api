import re
from test_case.get_data import *


#
# s = "hellowgaoengyi"
# res = re.match("(he)(ll)(o)", s)  # 全匹配，只匹配头部
# print("头部匹配结果的全部", res.group())  # 拿到匹配的字符进行分组group()=group(0)
# print("头部匹配结果的第二部分", res.group(2))  # 匹配了第二个分组的数据
#
# m = "hihigaomengyi"
# res = re.findall("(gao)(meng)", m)
# print(res)  # 匹配出来的结果是一个列表 在字符串里面找匹配的内容，存储到列表里面列表嵌套元组的方式
class DoRegx:
    @staticmethod
    def do_regx(l):
        while re.search("\$\{(.*?)\}", l):
            # print(res.group(1))  # 有一个括号代表一个分组，group(1)可以去掉{}
            key = re.search("\$\{(.*?)\}", l).group(0)
            value = re.search("\$\{(.*?)\}", l).group(1)
            """
            这个操作比较复杂分为两步
            第一步，去GetData中去找value的值，因为value的值在这里为tel_1，所以即为去GetData中去找tel_1的值
            第二步，找到tel_1的值后，将这个值与key值进行替换，这里的key为${tel_1},即为与这个值进行替换
            """
            l = l.replace(key, str(getattr(GetData, value)))
            print(key, value)
            print(l)
        return l


if __name__ == '__main__':
    l = '{"username": "${tel_1}", "password": "admin@123", "captcha": "", "remember":"true", "requestId": "", ' \
        '"code": ""} '
    res = DoRegx().do_regx(l)
