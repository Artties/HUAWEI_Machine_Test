#连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
#长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

#输入描述:
#连续输入字符串(输入多次,每个字符串长度小于100)

#输出描述:
#输出到长度为8的新字符串数组

def string_output(string):
    if len(string) <=8:
        print(string + "0" * (8 - len(string)))
    else:
        while len(string) > 8:
            string = string[8:] #Get the last characters after 8
            print(string + "0" * (8 - len(string)))
a=input()
b=input()
string_output(a)
string_output(b)

