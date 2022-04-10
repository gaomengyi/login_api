import pandas as pd

""""
介绍一下pandas中iloc和loc的区别和用法
1. loc使用范围比iloc更广更实用，loc可以使用切片、名称(index,columns)、也可以切片和名称混合使用；但是loc不能使用不存在的索引来充当切片取值,像-1
2. iloc只能用整数来取数
3.iloc是按照行数取值，而loc按着index名取值
"""

df = pd.read_excel('ht.xlsx', sheet_name='find')
print(df.values)  # 变成嵌套的列表数据，不指定sheet_name时，读取的是sheet1数据，指定的话读取该sheet页的数据

# 两种方法去除df中的1和3行
print("iloc结果：", df.iloc[1:3])
print("loc结果：", df.loc[0])
