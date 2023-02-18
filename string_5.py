## 格式化字符串 
## format 的用法
# year = 2010
# print("鱼C工作室成立于year年")
# print("鱼C工作室成立于{}年".format(year))
# print("1+2={},2的平方是{},3的立方是{}".format(1+2,2*2,3*3*3))
# print("{}看到{}就很激动！".format("布布","一二"))
# print("{1}看到{0}就很激动！".format("布布","一二"))
# print("{0}{0}{1}{1}".format("是","非"))

# print("我叫{name},我爱{fav}".format(name="小甲鱼",fav="Python"))
# print("我叫{name},我爱{0},喜爱{0}的人，运气哦都不会太差。".format("Python",name="小甲鱼"))

# print("{},{},{}".format(1,"{}",2))
# print("{},{{}},{}".format(1,2)) #也可以用{}注释{}

## {}内的：左边是索引值，右边是格式值
print("{:^10}".format(250))
print("{1:>10}{0:<10}".format(520,250))
print("{left:>10}{right:<10}".format(right=520,left=250))

## 在宽度width前加 0 可以用0填充并感知数字正负号
print("{:010}".format(250))
print("{:010}".format(-250))
## ：右边加任何字符都可以填充
print("{1:%>10}{0:%<10}".format(520,250))
print("{1:@>10}{0:@<10}".format(520,250))
print("{1:0=10}{0:0=10}".format(520,250))