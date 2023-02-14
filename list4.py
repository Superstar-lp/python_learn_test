# s = [1,2,3]
# t = [4,5,6];
# x = s+t
# print(x)
# y = x*3
# print(y)
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix)

# for i in matrix:
#     for each in i:
#         print(each)

# for i in matrix:
#     for each in i:
#         print(each,end=" ")
#     print()
# print(matrix[0])
# print(matrix[1][1])

A = [0]*3
for i in range(3):
    A[i]= [0] * 3
    
B=[[0]*3]*3             # B[0] is B[1] and B[1]is B[2]

A[1][1]=1
B[1][1]=2

print(A)
print(B)
