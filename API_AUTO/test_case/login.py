import os

import pytest

from test_case.get_data import GetData
from tool.http_request import Http_Request

"""
接口的关联性有三种方法：
1、反射
2、设置全局变量
3、存储到txt文件并读取
"""
Data = None  # 设置全局变量


class TestLogin:
    def test_user(self):
        url = "http://101.36.139.147:6339/ibps/user/login/apply"
        data = {"username": "admin", "password": "admin@123", "captcha": "", "remember": "true", "requestId": "",
                "code": ""}
        res = Http_Request().http_request("post", url, data)
        print(res.json())
        if res.json()['data']:
            # 反射如果res.json()['data']不为空，存储data在get_data.py文件中
            setattr(GetData, 'data', res.json()['data'])

    def test_authorize(self):
        global Data  # 声明全局变量
        url = "http://101.36.139.147:6339/ibps/authorize/apply"
        # 第一种方法中的反射，获取反射结果用getattr()
        data = {"login_state": getattr(GetData, 'data'), "client_id": "ibps"}
        res = Http_Request().http_request("post", url, data)
        print(res.json())
        # 第二种：使用全局变量
        # 如果res.json()['data']不为空，那么给全局变量中Data赋值
        if res.json()['data']:
            Data = res.json()['data']

    def test_authentication(self):
        url = "http://101.36.139.147:6339/ibps/authentication/apply"
        data = {"authorize_code": Data,
                "client_id": "ibps",
                "client_secret": "58b65297-3467-0859-8337-8cbaf81ef68a",
                "grant_type": "authorization_code"}
        res = Http_Request().http_request("post", url, data)
        print(res.json())
        print("cookie的值是：".format(res.cookies))
        access_token = res.json()['data']['access_token']
        refresh_token = res.json()['data']['refresh_token']
        print(f"[登录的access_token结果是]:{access_token}")
        print(f"[登录的refresh_token结果是]:{refresh_token}")
        # 第三种方法：给变量写入到txt文件中
        file = open("access_token.txt", "w+", encoding='utf-8')
        file.write(access_token)
        file = open("refresh_token.txt", "w+", encoding='utf-8')
        file.write(refresh_token)
        return access_token

    def test_username(self):
        file1 = open("access_token.txt", "r+", encoding='utf-8')
        a_token = file1.read()  # 读取文件中的所有数据
        file2 = open("refresh_token.txt", "r+", encoding='utf-8')
        r_token = file2.read()  # 读取文件中的所有数据
        url = "http://101.36.139.147:6339/ibps/user/context?username=admin"
        data = {"username": "admin"}
        # Cookie = {"ibps-3.3.9-release-lang": "zh-CN", "ibps-3.3.9-release-token": a_token,
        #           "bps-3.3.9-release-refresh_token": r_token, "ibps-3.3.9-release-uuid": '1'}
        header = {"X-Authorization-access_token": a_token}  # 其实主要是这个a_token是鉴权的 只要一直读取到这个数据就可以了
        # print("打印出来cookie值", Cookie)
        # 第三种方法：写入到txt文档中读取
        res = Http_Request().http_request("post", url, data, header)
        print(res.json())
        print("打印出来这个登录后的cookie", res.cookies)


if __name__ == '__main__':
    pytest.main(['login.py'])
