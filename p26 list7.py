# s = [[0]*3 for i in range(3)]
# s[1][1] = 1
# print(s)

# even = [i for i in range(10) if i%2 == 0]
# print(even)

# words = ["apple","banana","beautiful","fishc","fuck"]
# fword = [w for w in words if w[0] == "f"]
# print(fword)

##[expression for target1 in iterable1
#             for target2 in iterable2
#                   ……
#             for targetN in iterableN]

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# flatten = [col for row in matrix for col in row]
# print(flatten)

# xx =[x + y for x in "fishc" for y in "FISHC"]
# print(xx)
# _ = []                             # _ 可以用来作无关紧要的变量名
# for x in "fishc":
#     for y in "FISHC":
#         _.append(x +y)
# print(_)

##*****[expression for target1 in iterable1 if condition1
#                  for target2 in iterable2 if condition2
#                   ……
#                  for targetN in iterableN if conditionN]

# _=[[x,y] for x in range(10) if x%2 == 0 for y in range(10) if y%3 == 0]
# print(_)    # 与下式一样，将0-9之内被2整除的放在x位，被3整除的放在y位。

# _ =[]
# for x in range(10):
#     if x % 2 ==0:
#         for y in range(10):
#             if y % 3 == 0:
#                 _.append([x,y])
 
                