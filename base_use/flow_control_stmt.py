#!/usr/bin/env python
# encoding=utf-8

# if
# if的条件可以是数字或字符串或者布尔值True和False（布尔表达式）
# 如果是数字，则只要不等于0，就为true
# 如果是字符串，则只要不是空串，就为true
print("----if----")

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)

var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)
print("Good bye!")

# if else
var = 100
if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)
elif var == 100:
    print("3 - Got a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)

print("Good bye!")

# 嵌套if else
var = 100
if var < 200:
    print("Expression value is less than 200")
    if var == 150:
        print("Which is 150")
    elif var == 100:
        print("Which is 100")
    elif var == 50:
        print("Which is 50")
elif var < 50:
    print("Expression value is less than 50")
else:
    print("Could not find true expression")

print("Good bye!")

# while循环
print("----while----")
count = 0
while count < 5:
    print(count, " is  less than 5")
    count += 1
else:
    print(count, " is not less than 5")

# for循环
print("----for----")

# 求素数
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num/i
            print('%d equals %d * %d' % (num, i, j))
            break
    else:
        print(num, 'is a prime number')

# 遍历集合
r = range(10, 20)
r = {1, 2, 3, 4, 5}   # set类型
r = ["aaa", 3, "c"]
print(r)

for num in r:
    print(num)


r = {"a": 9, "b": 10}
print(r)

for num in r.values():
    print(num)


