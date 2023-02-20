# print("{:+}{:-}".format(520,-250)) # 负数默认自动加负号可以不用打
# print("{:,}".format(12345)) #千分符 ，
# print("{:_}".format(12345)) #千分符 _
# print("{:,}".format(1234124523425)) #千分符

# print("{:.2f}".format(3.1415))  #限制小数点后几位
# print("{:.2g}".format(3.1415))  #限制小数点左右一共几位
# print("{:.7}".format("I dislike fish"))
# ###print("{:.2}".format(520))#!整数不能使用精度！！！会报错


# print("{:b}".format(80))
# print("{:c}".format(80))
# print("{:d}".format(80))
# print("{:o}".format(80))
# print("{:x}".format(80))
# print("{:#x}".format(80))
# print("{:#b}".format(80))
# print("{:#d}".format(80))


print("{:e}".format(3.1415))
print("{:E}".format(3.1415))
print("{:f}".format(3.1415))
print("{:g}".format(123456789))
print("{:g}".format(1234.56789))
print("{:%}".format(0.98))
print("{:.2%}".format(0.98))
print("{:.{prec}f}".format(3.1315,prec =2))

print("{:{fill}{align}{width}.{prec}{ty}}".format(3.1415,fill = '+',align = '^',width = 10,prec = 3,ty = 'g'))

### f-string