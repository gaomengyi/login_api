s = "hellow"
print(s.find("h"))
print(s.find("m"))
# 找到的话返回的是索引
# 找不到返回-1
# new_s = s.replace("w", "gaomengyi")  # 用最后一个值w替换成gaomengyi
# print(new_s)
if s.find("hellow") != -1:  # 如果s里面能找到hellow 就执行下面结果
    print(s.replace("w", "gaomengyi"))
