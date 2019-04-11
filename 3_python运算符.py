#算术运算符

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

#比较运算符


a = 19
b = 21

print(a == b)
print(a != b)
# print(a <> b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#赋值运算符

a = 10
b = 20
c = 0

c = b
c += a
print(c)

c = b
c -= a
print(c)

c = b
c *= a
print(c)

c = b
c /= a
print(c)

c = b
c %= a
print(c)

c = b
c //= a
print(c)

c = b
c **= a
print(c)

print("----------------------------------")

#位运算符

a = 60
b = 13

print(a & b)
print(a | b)
print(a ^ b)
print(a >> b)
print(a << b)
print(~b)

#逻辑运算符

a = 10
b = 20

if a and b:
    print("1 - 变量 a 和 b 都为true")
else:
    print("1 - 变量 a 和 b 有一个不为true")

a = 0
# b = 0
if a or b:
    print("2 - 变量 a 和 b都为true或者有一个为true")
else:
    print("2- 变量 a 和 b都不为true")

if a and b:
    print("3 - 变量 a 和 b 都为true")
else:
    print("3 - 变量 a 和 b 有一个不为true")


if a or b:
    print("4 - 变量 a 和 b都为true或者有一个为true")
else:
    print("4- 变量 a 和 b都不为true")

if not (a and b):
    print("3 - 变量 a 和 b 都为true")
else:
    print("3 - 变量 a 和 b 有一个不为true")


#成员运算符
a = 10
list = [1, 2, 3, 4, 5, 6]
print(a in list)

print(a not in list)
#身份运算符

a = 10
b = 10

print(a is b)
print(a is not b)