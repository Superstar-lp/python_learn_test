## 列表推导式，速度更快
## 将列表中的每一个元素都变成原来的2倍
# oho = [1,2,3,4,5]
# for i in range(len(oho)):
#     oho[i] = oho[i]*2
# print(oho)

# oho = [i * 2 for i in oho]   # 一言以蔽之
# print(oho)

## [expreesion for target in iterable]
# x = [ i for i in range(10)]
# print(x)

# x = [ i+1 for i in range(10)]  #与18行列表追加一样的效果
# print(x)

# x = []
# for i in range (10):
#     x.append(i+1)
# print(x)

# y = [c*2 for c in "fishC"]
# print(y)

# code = [ord(c) for c in "fishC"] #oed是输出单个字符串相应的代码
# print(code)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# col2 = [row[1] for row in matrix]
# print(col2)

diag = [matrix [i][i] for i in range(len(matrix))]
print(diag)

diag2 = [matrix[i][2-i] for i in range(len(matrix))]
print(diag2)