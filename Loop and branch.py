###Loop and branch 1
# if 3 > 5:
#     print ("我在里面")
#     print("我在外面")
# print("我真在外面")

# 多条件分支
# score = input("请输入分数：")
# score = int(score)

# if 0 <= score< 60:
#     print("D")
# elif 60<= score <80:
#     print("C")
# elif 80<= score <90:
#     print("B")
# elif 90<= score <100:
#     print("A")
# elif score==100:
#     print("S")
# else:
#     print("请输入0~100的分值！")

###Loop and branch 2
# age = 16
# print("抱歉，未满18岁禁止访问") if age < 18 else print("欢迎您来")

# score = 66
# level = ('d' if 0<= score <60 else
#          'c' if 60 <= score< 80 else 
#          'b' if 80 <= score< 90 else 
#          'a' if 90 <= score< 100 else 
#          's' if score== 100     else
#          print("请输入正确的数值！") )
# print(level)

###Loop and branch 3   python代码要严格对齐qaq
# life ="yes"
# while life == "yes":
#     life = input("今天你还活着嘛？")

# while True:
#     answer = input ("你要推出循环吗？")
#     if answer == "可以！":
#             break
#     print("好累")

    ###Loop and branch 4
##continue 跳出本轮循环
# i = 1
# while i < 5:
#     print("循环内i的值是",i)
#     i += 1
# else:
#     print("循环外，i的值是",i)

# i = 1
# while i < 5:
#     print("循环内i的值是",i)
#     i += 1
# print("循环外，i的值是",i)

# i = 1
# while i < 5:
#     print("循环内i的值是",i)
#     if i == 2:
#          break
#     i += 1
# else:
#     print("循环外，i的值是",i)
## while  break else 的应用，只有完整把while走完才会使用else，如果中间break了，那么就不会执行else！
# day =1
# while day <= 7:
#     answer = input("今天又好好学习嘛？")
#     if answer != "有":
#         break
#     day += 1
# else:
#     print("非常好，你已经坚持学习了7天学习！")

## 9*9乘法表
# i = 1
# while i<=9:
#     j = 1
#     while j<= i:
#         print(j,"*",i,"=",j*i,end=" ")
#         j += 1
#     print()
#     i += 1

### break 每次只跳出一层循环体  