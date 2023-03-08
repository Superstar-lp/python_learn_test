# 莫斯密码对比表
# c_table = [".-","A","-..","B","-.-.","C","-..","D",".","E","..-.","F",
#            "--.","G","....","H","..","I",".---","J","-.-", "K",".-..", "L",
#            "--","M","-.","N","---","O",".--.","P","--.-","Q",".-.","R",
#            "...","S","-","T","..-","U","...-","V",".--","W","-..-","X",
#            "-.--","Y","--..","Z",".----","1","..---","2","...--","3","....-","4",
#            ".....","5","-....","6","--...","7","---..","8","----.","9","-----","0"]


# code = input("请输入摩斯密码：")
# split_code = code.split(" ")

# result = [c_table[c_table.index(each) + 1] for each in split_code]
# print (result)
# #... .... .- -. --. .... .- .. --.. .. .-.. .- .. ... .... ..- .. .-.. .- .. --.. .. .... .- .. ... .... .- -. --.

# 字典的方法↓↓↓
# 莫斯密码对比表
c_table = {".-":"A","-..":"B","-.-.":"C","-..":"D",".":"E","..-.":"F",
           "--.":"G","....":"H","..":"I",".---":"J","-.-": "K",".-..": "L",
           "--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R",
           "...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X",
           "-.--":"Y","--..":"Z",".----":"1","..---":"2","...--":"3","....-":"4",
           ".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0"}


code = input("请输入摩斯密码：")
split_code = code.split(" ")

result = [c_table[each] for each in split_code]
print (result)