print(type({}))
type({"one"})
#创建集合的三个方法

{"fishc","python"}
print({s for s in "fishc"})  #集合是无序的，没办法下标索引
print(set("Fishc"))

#利用集合检查是否有重合元素
s = [1,1,2,3,4]
len(s) == len(set(s))  #因为set会让数组变成集合，且不重复，所以只有四个元素了，比较之前的长度就知道是否存在重复元素
# 浅拷贝
t = s.copy()

# 检测是否相关
s = set("Fishc") #都有h，所以是相关的
print(s.isdisjoint(set("JAVA")))#s与java 没有相同的字母所以是false
#检测是否是另一个集合的子集
print(s.issubset("Fishc.com"))
#检测是否是另一个集合的超集
print(s.issuperset("Fish"))

# 集合并集 union
print(s.union({1,2,3}))

#交集
s.intersection("fish")
#差集
s.difference("Fish")

#上面三个函数都是多参数的，可以好几个一起运算
s.union({1,2,3},"Python")

# 以下是上面运算的快捷字符，需要注意的是，使用字符运算必须两边都是集合类型；函数是支持任何可迭代对象的
s<= set("FishC")
s < set("Fishc")
s > set("Fishc")
s >= set("Fishc")
s |{1,2,3}|set("python")
s & set("php") & set("python")
s - set("php") - set("python")
s ^set("Python") #对称差集