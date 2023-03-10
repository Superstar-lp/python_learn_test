# d = dict.fromkeys("FishC")
# print(d)
# d['s']=115
# print(d)

# # update([other])
# d.update({'i':105,'h':104})
# print(d)
# d.update(F='70',C='67')
# print(d)

# ## 查
# d['s']
# print(d.get('c',"这里没有c"))

# print(d.setdefault('C',"code"))
# print(d.setdefault('c',"code"))
# print(d)

# ##  items()、keys()  values()
# keys = d.keys()
# values = d.values()
# items = d.items()
# print(items)
# print(keys)
# print(values)
# d.pop('c')
# print(items)
# print(keys)
# print(values)

# # copy()
# e = d.copy()
# print(e)

# # len() 获取字典中键值对的数量
# len(d)
# # 用 in 和 not in 判断键是否在字典中
# 'C' in d
# "c" not in d
# print(list(d))

# e = iter(d)   # 迭代器
# print(next(e))
# print(next(e))
# print(next(e))

# print(list(reversed(d.values())))

# d = {"吕布":{"语文":60,"数学":70,"英语":80}, "关羽": {"语文":80, "数学":90,"英语":70}}
# print(d["吕布"]["数学"])
d = {"吕布":{60,70,80}, "关羽": {80, 90,70}}
print(d["吕布"][1])