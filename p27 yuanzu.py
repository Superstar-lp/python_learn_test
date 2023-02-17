# rhyme = (1,2,3,4,5,"上山打老虎")
# print(rhyme)
# rhyme = 1,2,3,4,5,"下山捉兔子"
# print(rhyme)
# print(rhyme[0],rhyme[-1])   

# ##rhyme[1] = 10 # 元组的元素不能修改，但是可以切片（不是修改）
# print(rhyme[3:])
# print(rhyme[::2])

# nums = 3,1,9,6,8,3,5,3
# print(nums.count(3))

# heros = ("蜘蛛侠","绿巨人","黑寡妇")
# heros.index("黑寡妇")

# s = (1,2,3)
# t = (4,5,6)
# z = s*3
# y = (s,t)
# print(z," ",y)

#### 生成一个元组我们有时候也称之为元组的打包 

# t = (123,"FishC",3.14)
# print(t)
# ### 把一个元组的元素一次性分给其他变量的过程称之为 解包
# x,y,z = t
# print(x," ",y," ",z)
# a,b,*c = "FishC"
# print(a)

# print(b)

# print(c)

# x,y = 10,20
# print(x,y)

s = [1,2,3]
t = [4,5,6]
w = (s,t)
print(w)
w[0][0] = 0
print(w)
