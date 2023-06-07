t = frozenset("Fishc")  # 不可变的集合
s = set("Fishc")

# update（） 可以根据括号内函数更新集合
s.update([1,1],"23")
print(s)  #可以看到虽然插入了一个列表[1,1]但是集合元素是不重复的，所以只有一个1，而且也是无序的。
# t.update([1,1],"23")  #而对于这个集合使用次函数就会报错，因为不可改变

s.intersection_update("FishC")
print(s)
s.difference_update("Php","Python")
print(s)
s.symmetric_difference_update("python")
print(s)

#单纯添加一个数据到集合内
s.add("45")
print(s) #不同与直接update的是，add是添加整个字符串，update是每个字符插入集合。

# s.remove("没有")
s.discard("没有")

s.pop()#随机弹出一个元素，这里没有打印所以运行看不到。

s.clear() #清空集合内元素
