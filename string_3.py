###  判断和检测   返回布尔类型的值
# startswith(prefix[,start[,end]]) 判断指定字符串是否出现在字符串的起始位置
# endswith(suffix[,start[,end]]) 判断指定子字符串是否出现在字符串的结束位置
## 函数里含有方括号是可选参数，相当于高级定制版，start 和end 都可以选择索引下标

# isupper()是否所有字母都是大写字母
# islower()是否所有字母都是小写字母

# istitle() isalpha() isascii() isspace() isprintable()
# isdecimal() isdigit() isnumeric() isalnum() isidentifier()

# x = "我爱Python"
# print(x.startswith("我"))
# print(x.startswith("小甲鱼"))
# print(x.endswith("Python"))
# print(x.startswith("我",1))
# print(x.startswith("爱",1))
# print(x.endswith("Py"))
# print(x.endswith("Py",0,4))

# x = "她爱Python"
# if x.startswith(("你","我","她")):   #要用元组作为匹配项的话不要忘记加上括号
#     print("总有人爱Python")
    
    
# # istitle()  测试是否字符串的所有单词都是大写字母开头，其余字母均为小写
# _ = "I love Python"
# print(_.istitle())

# # isupper() 是否所有字母都是大写字母
# print(_.isupper())
# print(_.upper().isupper())  #从左到右依次调用  

# # isalpha() 是否都是字母构成，空格也不是字母
# print(_.isalpha())

# #isspace() 是否是空白字符串
# #isprintable() 字符串中的字符是否都是可打印的(转义字符不能打印)
# print("i love fishc\n".isprintable())

# isdecimal() isdigit() isnumeric()  三个函数检测数字的尺度和范围递增 注意字符串之间不能有空格
x = "12345"
y = "2²"
z = "一二三"
r = "ⅠⅡⅢ"
print(x.isdecimal(), x.isdigit(), x.isnumeric())
print(y.isdecimal(), y.isdigit(), y.isnumeric())
print(z.isdecimal(), z.isdigit(), z.isnumeric())
print(r.isdecimal(), r.isdigit(), r.isnumeric())

#isalnum() 是如果isdecimal() isdigit() isnumeric() isalpha() 之中任意一个返回True 即返回 True
# isidentifier() 判断字符串是否是一个合法的python标识符

print("I am a good gay".isidentifier())
print("I_am_a_good_gay".isidentifier())

## 可以通过 import keyword 模块 判断字符串是否是python保留字符串
import keyword
print(keyword.iskeyword("if"))
print(keyword.iskeyword("py"))