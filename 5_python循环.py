#循环

list = [1, 2, 3, 4, 5, 6]

one = []
two = []

while len(list) > 0:
    numbers = list.pop()
    if (numbers % 2 == 0):
        one.append(numbers)
    else:
        two.append(numbers)


print(one)
print(two)


count = 0

while count < 9:
    print("数字" + str(count))
    count+=1


count = 20
while count:
    count -= 1
    if count % 2 == 0:
        continue #跳出本次循环执行下次循环
    print(count)


count = 20
while count:
    count -= 1
    if count % 2 == 0:
        break#跳出循环
    print(count)

count = 1
# while count:
#     num = input("您输入的是 : ")
#     print("您输入的是 " + num)


count = 2
while count:
    print(count)
    count-=1
else:
    print("您的程序进入else")

print("结束")