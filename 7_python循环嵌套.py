
# python循环嵌套
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print(i,"是素数"),
   i = i + 1



for i in range(1,10):
    for j in range(1,i + 1):
        print(j,"*",i,"=",i*j," ",end='')
    print()