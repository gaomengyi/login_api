import logging

# logger 收集日志 debug
# handdler 输出日志的渠道 指定文件还是控制台 默认是控制台
#
# logging.debug("高梦依debug")
# logging.info("高梦依info")
# logging.warning("高梦依warning")
# logging.error("高梦依error")
# logging.critical("gaomengyi cri")


# 定义一个日志收集器 my_logger
my_logger = logging.getLogger("pythonmm")
# 设定级别
my_logger.setLevel("DEBUG")

# 设置输出格式
fommart = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
# 创建自己的输出渠道
ch = logging.StreamHandler()
ch.setLevel("ERROR")  # 设置级别在error及以上才会输出到控制台
fh = logging.FileHandler("loggin.txt", encoding='utf-8')  # 输出结果在loggin.txt文件夹
# 设置格式写入到txt文件中
fh.setFormatter(fommart)

# 两者对接----指定输出渠道
my_logger.addHandler(ch)
my_logger.addHandler(fh)
# 收集日志
my_logger.debug("懵逼了哈哈哈debug")
my_logger.error("gmmerror")
