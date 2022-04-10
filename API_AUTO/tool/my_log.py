import logging
from tool.project_path import *

class Mylog:
    def my_log(self, level, msg):
        # 定义一个日志收集器 my_logger
        my_logger = logging.getLogger("pythonmm")

        # 设定级别
        my_logger.setLevel("DEBUG")

        # 设置输出格式
        fommart = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')

        # 创建自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel("ERROR")  # 设置级别在error及以上才会输出到控制台
        fh = logging.FileHandler(logging_path, encoding='utf-8')  # 输出结果在loggin.txt文件夹

        # 设置格式写入到txt文件中
        fh.setFormatter(fommart)
        ch.setFormatter(fommart)

        # 两者对接----指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "INFO":
            my_logger.error(msg)
        elif level == "WARING":
            my_logger.error(msg)
        elif level == "CRITICAL":
            my_logger.error(msg)

        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log('DEBUG', msg)  # 调用my_log方法

    def info(self, msg):
        self.my_log('INFO', msg)

    def error(self, msg):
        self.my_log('INFO', msg)

    def critical(self, msg):
        self.my_log('INFO', msg)


if __name__ == '__main__':
    log = Mylog()
    log.debug("可以吗")
    log.info("试一试")
