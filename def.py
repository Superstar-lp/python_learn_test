def temp_conv(c):
    f = c*1.8 + 32
    return f



c = float(input("请输入摄氏度："))
f = temp_conv(c)
print("转化成华氏度是：" + str(f))
 