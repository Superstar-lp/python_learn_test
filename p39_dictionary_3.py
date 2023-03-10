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
# d = {"吕布":[60,70,80], "关羽": [80, 90,70]}
# print(d["吕布"][1])

# 字典推导式
d = {'F':70,'i' :105, 's':115, 'h' :104, 'C':67}
b = {v:k for k,v in d.items()}
print(b)
c = {v:k for k,v in d.items() if v > 100}
print(c)
d = {x:ord(x) for x in "FishC"}
print(d)
e = {x:y for x in [1,3,5] for y in [2,4,6]}  #!! 键不会存重复的！！ 所以2，4被后面传入的6替代掉了，分为两次循环看就比较简单了
print(e)