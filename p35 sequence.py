# 跟序列相关的一些函数

## 列表、元组、字符串相互转换的函数
## list(),tuple(),str()

# print(list("FishC")," ",list((1,2,3,4,5)))
# print(tuple("FishC")," ",tuple([1,2,3,4,5]))
# print(str( (1, 2, 3, 4,5))," ",str([1,2,3,4,5]))

## 对比传入的参数，并返回最小值和最大值
## min()&max()
# s = [1,1,2,3,5]
# print(min(s))
# t = "FishC"
# print(max(t))
# s = []
# print(min(s)) # 传入空的参数会报错
# print(min(s,default = "屁，啥都没有，怎么找到最小？"))
# print(min(1,2,3,0,6)) 


##  len() & sum()
# a = len(2 ** 100)   len函数的参数有上限
# s = [1,0,0,8,6]
# print(sum(s))
## sum 有一个 start参数 用于指定求和计算的起始值
# print(sum(s,100))



## sorted() & reversed() 
# s = [1,2,3,0,6]
# print(sorted(s))   # sorted()不改变原来的序列
# print(s)
# print(s.sort())
# print(s)

# s = [1,2,3,0,6]
# print(sorted(s,reverse=True)) 

t = ["FishC","Apple","Book","Banana","Pen"]
a = sorted(t)            #默认是比较每个字符串的首字母的ascii值，一样则比较下一个字母的ascii值
b = sorted(t,key=len)    # key用len的时候是比较字符串的长度
print(a,"\n",b)
t.sort(key=len)       #列表的.sort只对列表有效 而sorted()函数可以接受任何形式的可迭代对象作为参数 reversed 也是
print(t)
print(sorted("FishC"))
print(sorted((1,0,0,8,6)))
s = [1,2,5,8,0]
a = reversed(s)
# # print(a)
print(list(reversed("FishC")))
print(list(reversed((1,2,5,9,3))))
print(list(reversed(range(0,10))))