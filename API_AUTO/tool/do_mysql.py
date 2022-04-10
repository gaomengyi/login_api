"""
关键字参数的传递

"""
import pymysql
import MySQLdb
from tool.project_path import *
from tool.get_config import *


# 参数整理

class DoMysql:
    def do_mysql(self, query_sql, state="all"):  # query_sql是查询语句，state是查询一行或者多行数据的配置
        db_config = eval(ReadConfig().read_config(caseini_path, "DB", "db_config"))
        # 创建一个数据库连接
        cnn = MySQLdb.connect(**db_config)
        # print(cnn)
        # 关键字参数的传递

        # 创建一个游标cursor
        cursor = cnn.cursor()

        # 写sql语句--字符串
        # query_sql = 'SELECT PROC_DEF_ID_ FROM act_hi_actinst WHERE ID_>488757228828884992'

        # 执行语句
        cursor.execute(query_sql)

        # 获取结果 打印结果
        if state == 1:
            res = cursor.fetchone()  # 针对一条数据的读取
        else:
            res = cursor.fetchall()  # 元组 针对多条数据 元组嵌套元组
        print(res)
        # print(type(res))
        # 关闭连接
        cnn.close()
        return res


if __name__ == '__main__':
    query_sql = 'SELECT PROC_DEF_ID_ FROM act_hi_actinst WHERE ID_>488757228828884992'
    res = DoMysql().do_mysql(query_sql)
    print(res[0][0])  # 取到第一个元组，再取一层第一个元组中的第一个数据
    from test_case.get_data import GetData

    # 利用反射获取到init表格中的id数据，再根据id进行数据库中查询
    query_sql2 = "SELECT * FROM `act_ru_task` WHERE ID_={0}".format(eval(getattr(GetData, "id")))
    # 根据元组取值
    loan_id = DoMysql().do_mysql(query_sql2)[0][2]
    print(loan_id)
