# # all() & any()     是否所有元素为真  和  是否存在某个元素为真
# x= [1,1,0]
# y = [1,1,9]
# print(all(x))
# print(any(y))


## enumerate()   有一个start参数可以使用指定序列开始序号
# seasons = ["spring","summer","Fall","winter"]
# # print(enumerate(seasons))  #需要通过列表给他转化一下
# print(list(enumerate(seasons))) 
# print(list(enumerate(seasons,10))) 

## zip 
# x = [1,2,3]
# y = [4,5,6]
# zipped = zip(x,y)
# print(list(zipped))
# z= [7,8,9]
# zipped = zip(x,y,z)
# print(list(zipped))

# _ = "fishc"
# zipped = zip(x,y,_)  # 以最短的划分元组数 只有三个元素 可以通过导入工具函数以最长的划分元素
# print(list(zipped))
# import itertools
# zipped = itertools.zip_longest(x,y,_)
# print(list(zipped))

# map 对传入的可迭代对象的每一个元素进行计算并传回对象中
# mapped = map(ord,"fishC")    # ord函数是字符转换为编码
# print(list(mapped))
# mapped = map(pow,[2,3,10],[5,2,3])  #相当于[pow(2,5),pow(3,2),pow(10,3)]
# _ = list(mapped)
# print(_)
# mapped = map(max,[1,3,6],[0,2,7],[2,2,9,9])
# print(list(mapped))

# # filter() 与map类似，但是返回的是结果为真的元素
# print(list(filter(str.islower,"FishC")))

# mapped = map(ord,"fishC")
# for each in mapped:
#     print(each)
# print(list(mapped))    #所以迭代器只能用一次

x = [1,2,3,4,5]
# y = iter(x)
# print(type(x),type(y))
# for i in range(6):    #异常是因为取了6次，迭代器取了5次之后就没了
#     print(next(y))     #next是用来取迭代器里的元素的函数，可以增加参数在迭代器取完后显示
z = iter(x)
for i in range(7):    #异常是因为取了6次，迭代器取了5次之后就没了
    print(next(z,"没啦，掏空了~"))
    