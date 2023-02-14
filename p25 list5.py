## list copy  : shallow and  deep

# x = [1,2,3]
# y = x.copy()
# x[1]=1 #修改x列表的第二个元素，看看y列表有无变化
# print(x)
# print(y) #可以看到y列表的元素没变化

##通过切片的方法浅拷贝
# x = [1,2,3]
# y = x[:]
# x[1]=1
# print(x)
# print(y)


# x =[[1,2,3],[4,5,6],[7,8,9]]
# y = x.copy()
# x[1][1] = 0
# print(x)
# print(y)     #可以看到无法拷贝一个全新的嵌套列表

# import copy
# x =[[1,2,3],[4,5,6],[7,8,9]]
# y = copy.copy(x)
# x[1][1] = 0
# print(x)
# print(y) 

## depp copy    copy.deepcopy()
import copy
x =[[1,2,3],[4,5,6],[7,8,9]]
y = copy.deepcopy(x)
x[1][1]=0
print(x)
print(y)