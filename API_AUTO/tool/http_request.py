import requests

""""
封装请求方法
"""


class Http_Request:
    def http_request(self, method, url, data=None, header=None, cookie=None, ):
        sess = requests.session()  # 创建一个会话
        try:
            if method.lower() == "get":
                res = sess.get(url, params=data, headers=header, cookies=cookie, verify=False)
            else:
                res = sess.post(url, json=data, headers=header, cookies=cookie, verify=False)
        except Exception as e:
            print("请求出错了".format(e))
            raise e
        return res


if __name__ == '__main__':
    res = Http_Request()
    url = "http://101.36.139.147:6339/ibps/form/def/getFormData?templateKey=htyyzs&formKey=yysqxq&pk=946731856072540160&rightsScope=data"
    data = {"templateKey":"tyhtqc","formKey":"tyhtspb","pk":946731856072540160,"rightsScope":"data"}
    print(type(data))
    result = res.http_request('post', url, data)
    print(result.json())
