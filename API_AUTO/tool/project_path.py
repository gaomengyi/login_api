"""
专门读取路径的值
"""
import os

# 给绝对路径切割，变成一个元组为('E:\\pycharm\\code\\ningmeng\\API_AUTO\\tool', 'project_path.py')
# 定位到根目录
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(type(project_path))
print(project_path)
# 测试用例的绝对路径
testcase_path = os.path.join(project_path, "test_case\\ht.xlsx")
# print(testcase_path)
# 测试报告的绝对路径
report_path = os.path.join(project_path, "test_result\\html_report", "test.html")
# 配置文件地址1
caseini_path = os.path.join(project_path, "conf", "case.ini")
# print(caseini_path)
# 配置文件地址2
test_caseini_path = os.path.join(project_path, "conf", "test_case.ini")
# loggin文件的地址
logging_path = os.path.join(project_path, "test_result\\logs", "loggin.txt")
