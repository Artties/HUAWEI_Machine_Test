def string_output(string):
    if len(string) <=8:
        print(string + "0" * (8 - len(string)))
    else:
        while len(string) > 8:
            print(string[:8])
            string = string[8:]
            print(string + "0" * (8 - len(string)))
a=input()
b=input()
string_output(a)
string_output(b)