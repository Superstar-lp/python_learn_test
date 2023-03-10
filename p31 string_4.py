### strip(chars = None) lstrip(chars = None) rstrip(chars = None) removeprefix(prefix) removesuffix(suffix)

# # lstrip() 去掉字符串左侧的空白
# print("        左侧不要留白".lstrip())

# # rstrip() 去掉字符串右侧的空白
# print("右侧不要留白         ".rstrip())

# # strip()  去掉左右侧的空白
# print("       左右不要留白          ".strip())

# # 以上三个函数都可以设定指定参数,从指定一测匹配字符串的字母直到第一个匹配不了的字母停止
# print("www.ilovefishc.com".lstrip("wcom."))
# print("www.ilovefishc.com".rstrip("wcom."))
# print("www.ilovefishc.com".strip("wcom."))

# #removeprefix(prefix) removesuffix(suffix)
# print("www.ilovefishc.com".removeprefix("www."))
# print("www.ilovefishc.com".removesuffix(".com"))

## partition(sep)  rpartition(sep) 将字符串以参数指定的分割符为依据进行切割，并且将切割后的结果返回一个三元组
# print("www.ilovefishc.com".partition("."))
# print("www.ilovefishc.com".rpartition(".")) # 从右到左找分割符
# _ = "苟日新，日日新，又日新"
# print(_.split())

# _ = "苟日新 日日新 又日新"
# print(_.split())

# _ = "苟日新，日日新，又日新"
# print(_.split('，'))
# print(_.split('，',1))
# print(_.rsplit('，',1))

# ## splitlines()  ####  按 行 把字符串进行分割
# x = "苟日新\n日日新\n又日新"
# y = "苟日新\r日日新\r又日新"
# z = "苟日新\n日日新\r又日新"
# print(x.splitlines())
# print(y.splitlines())
# print(z.splitlines())

# print(x.splitlines(True))#参数为Tru 时保存换行字符


##### join(iterable)     把前面的分割符插入到几个字符串之中
x = ".".join(["www","ilovefishc","com"])
print(x)
y = "^".join(["F","ish","C"])
print(y)

# 拼接字符串的时候也可以用 join ，比直接用+拼接效率更快
z = "FishC"
z += z
print(z)

r = "FishC"
r = "".join(("FishC","FishC"))
print(r)