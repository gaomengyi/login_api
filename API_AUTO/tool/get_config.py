# encoding=utf-8
import configparser
import os
from tool.project_path import *

"""
读取配置文件的数据
"""


class ReadConfig:
    @staticmethod
    def read_config(filename, section, option):
        cf = configparser.ConfigParser()  # 创建一个实例cf 调用conconfigparser模块中的ConfigParser类
        cf.read(filename, encoding='utf-8')  # 调用ConfigParser类中read方法
        # print(cf.get(section, option))  # 调用ConfigParser类中get方法
        # print(type(cf.get(section, option)))  # 读取的配置文件都是str类型
        return cf.get(section, option)


if __name__ == '__main__':
    rd = ReadConfig.read_config(test_caseini_path, 'MODE', 'mode')
    print(rd)
    print(type(rd))  # 从字典里面读取的数据是str格式
    print(ReadConfig.read_config(caseini_path, 'MODE', 'button'))
    print(type(ReadConfig.read_config(caseini_path, 'MODE', 'button')))
