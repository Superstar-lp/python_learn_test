#a = [1,2,3,4,5,'上山打老虎']
# for each in a:
#     print(each)

# print(a[0],a[1],a[2],a[3])
# print()
# print(a[-1],a[-2],a[-3])
# print(a[0:3])
# print(a)
# print(a[0:6:2])
# print(a[::2])
# print(a[::-1])


##list 2
## 增 删 改 查
# heros = ["iron man","big green man"]
# heros.append("black woman") #只添加一个元素进列表里使用append
# heros.extend(["ice","flash","superman"])#添加两个以上元素进列表使用extend
# print(heros)

# s = [1,2,3,4,5]
# s[len(s):]=[6]
# print(s)
# s[len(s):]=[7,8,9]
# print(s)

# s = [1,3,4,5]
# s.insert(1,2)
# print(s)
# s.insert(0,0)
# s.insert(len(s),6)
# print(s)

# heros.remove("flash")   #remove删除已有的名称的元素，的其中一个
# print(heros)
# heros.pop(2)            #pop删除指定下标的元素。从0开始。
# print(heros)

# heros[4] = "钢铁侠"
# print(heros)
# heros[3:]=["灰太狼","喜羊羊","小灰灰"]
# print(heros)

nums = [3,1,9,6,8,8,5,4]
nums.sort()                   
print(nums)
nums.reverse()
print(nums)                   
print(nums.count(3))
print(nums.index(5))
nums2 =nums                  #直接列表赋值不能复制一个新的列表，只是把一个列表取了两个名字。
nums2.insert(0,100)
print(nums2)
print(nums)
nums3=nums.copy()
nums3.insert(0,99)
print(nums3)
print(nums)