# 创建和定义函数
# def myfunc():
#     pass
# myfunc()

def myfunc():
    for i in range(3):
        print("I love Y")

myfunc()

# 函数的参数
def myfunc2(name):
    for i in range(3):
        print(f"I love {name}") # f 是识别格式

myfunc2("food")

def myfunc3(name,times):
    for i in range(times):
        print(f"I love {name}")

myfunc3("python",5)

#函数的返回值

def div(x,y):
    z = x/y
    return z

def div2(x,y):
    return x/y

def div3(x,y):
    if y==0:
        return "除数不能为0！"
    else:
        return x/y
    
def div4(x,y):
    if y==0:
        return "除数不能为0！"
    return x/y

print(div(4,2))
print(div4(3,0))
print(div4(22,7))