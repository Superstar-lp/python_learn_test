## 字符串查找功能 
## count(sub[,start[,end]])用于查找指定字符串在指定区间内的出现次数
# x = "上海自来水来自海上"
# print(x.count("海"))
# print(x.count("海",0,5))

## find(sub[,start[,end]])   给出指定区间内，指定字符串的从左到右第一次出现的下标。
## rfind(sub[,start[,end]])  给出指定区间内，指定字符串的从右到左第一次出现的下标。
# print(x.find("海"))
# print(x.rfind("海"))
# print(x.index("海"))


##  替换   expandtabs([tabsize=8]) 使用空格代替制表符并返回一个新的字符串   replace(old,new,count=-1)  translate(table)
# code = """
#     print("I love FishC")
#     print("I LOVE wife")"""
# new_code = code.expandtabs(6)
# print(new_code)

# print("在吗！我在你家楼下！".replace("在吗","想你"))

## translate(table) 相当于是根据密码本转换，前面一串是原码 后面一串是译码 还可以加入第三个参数 忽略指定的字符串
table = str.maketrans("ABCDEFG","1234567") 制表
print("I love FishC".translate(table))
print("I love FishC".translate(str.maketrans("ABCDEFG","1234567")))
print("I love FishC".translate(str.maketrans("ABCDEFG","1234567","love")))