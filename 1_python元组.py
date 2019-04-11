

# python元组

list = ("chenweilong",1,3.1415926,"longbaba")
tlist = ("tlist",123)
print(list)#输出完整元组
print(list[0])#第一个
print(list[0:3])#第一个到第三个
print(list[1:])#到结尾
print(tlist * 2)
print(list +  tlist)
list[0] = "longlong"#元组元素不可改变 他是只读的