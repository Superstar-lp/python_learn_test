# a = [1,2,3]+[4,5,6]
# b = (1,2,3)+(4,5,6)
# c = "123"+"456"
# d = [1,2,3]*3 #重复
# e = (1,2,3)*3
# f = "123"*3
# s = [1,2,3]
# g = id(s)   #id是找到对象的“身份证”
# print(g)
# s *=2
# print(s)
# g=id(s)
# print(g)
# t = (1,2,3)
# print(id(t))
# t *=2
# print(id(t))
# _ = "fish"
# __ = "fish"
# print(_ is __)   # is 是判断两个变量是否指向同一个对象
# _ = [1,2,3]
# __= [1,2,3]
# print(_ is __) 

# print("鱼" in "鱼C")
# print("fish" in "fishC")
# print("fish" not in "fishC")

# x = "FishC"
# y = [1,2,3]
# del x,y
# print(x)
# x= [1,2,3,4,5]
# del x[1:4]      # python 里都是包头不包尾，所以这里删除 1，2，3指向的第2，3，4个元素
# print(x)

## 用切片也可以删除元素
# y = [1,2,3,4,5]
# y[1:4]=[]
# print(y)

x = [1,2,3,4,5]
del x[::2]
print(x)

x = [1,2,3,4,5]
x.clear()
print(x)
y = [1,2,3,4,5]
del y[:]
print(y)
