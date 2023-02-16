# x = "12321"
# print("是回文数") if x == x[::-1] else print("不是回文数")

z = "I like By bike"
print(z.casefold()," ",z.capitalize()," ",z.upper()," ",z.swapcase()," ",z.lower()," ",z.title())

## 上面的六个是改变字母大小写的，下面的四个是用来对齐的，括号内第二个变量可填充增加的元素
x = "有内鬼，停止交易！"
print(x.center(5))
print(x.center(15))
print(x.ljust(15))
print(x.rjust(15))
print(x.zfill(15))
print(x.center(15,"淦"))
print(x.ljust(15,"淦"))
print(x.rjust(15,"淦"))

