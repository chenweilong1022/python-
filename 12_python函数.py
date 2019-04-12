
# python函数

def add(str):
    return str + "chenweilong"


var = add("woshi")
print(var)


# 测试python值传递


def change(i):
    i = 20
    print(i)

a = 11
print(a,"1")
change(a)
print(a,"3")
# python数字传递到方法内部值不会改变
import math
def changelist(list):
    list[0] = "long"
    list[2] = math.pi


list = [0,1,2,3,4,5,6]

print(list)
changelist(list)
print(list)

# 必备参数

def printlocal(str):
    print(str)

#printlocal()#必备参数

# 关键字参数
printlocal(str="longbaba")

def person(name,age):
    printlocal(name)
    printlocal(age)

person(age=11,name="longlong")

def defaultpar(name="long"):
    printlocal(name)


defaultpar()

def ranpar(*num):
    printlocal(num)
    for n in num:
        printlocal(n)

ranpar(1,2,3,4)

sum = lambda var1,var2:var1 + var2

printlocal(sum(10,20))
