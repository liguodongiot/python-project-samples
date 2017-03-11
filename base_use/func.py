# coding=utf-8

def changeme(mylist):

    mylist.append([1, 2, 3, 4])
    print("Values inside the function: ", mylist)
    return

# 调用函数
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)

