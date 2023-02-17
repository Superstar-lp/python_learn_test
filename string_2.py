## 字符串查找功能 
## count(sub[,start[,end]])用于查找指定字符串在指定区间内的出现次数
x = "上海自来水来自海上"
print(x.count("海"))
print(x.count("海",0,5))

## find(sub[,start[,end]])   给出指定区间内，指定字符串的从左到右第一次出现的下标。
## rfind(sub[,start[,end]])  给出指定区间内，指定字符串的从右到左第一次出现的下标。
print(x.find("海"))
print(x.rfind("海"))

print(x.index("海"))
