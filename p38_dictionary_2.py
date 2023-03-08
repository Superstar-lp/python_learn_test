# y = {"吕布":"口口布","关羽":"关习习"}
# print(type(y))
# print(y["吕布"])
# y["刘备"] = "刘Baby"
# print(y)
## 六种创建字典的方法见笔记

## 字典也可以增删改查
# formkeys(iterable[,values])  使用 iterable 指定的可迭代对象来创建一个新的字典，并将所有的值初始化为 values 参数指定的值

# d = dict.fromkeys("Fish",250)
# print(d)
# d['F'] = 70   #'' "" 都可以
# print(d)
# d['C'] = 67
# print(d)


# # 删
# d.pop('s')
# print(d)
# d.pop("狗","没有")

# del d['h']
# print(d)

# del d
# print(d)

d = dict.fromkeys("Fish",250)
d.clear()   #清空字典但是不删除
print(d)