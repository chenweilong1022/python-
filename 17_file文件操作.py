

file = open("D:/log/test_java_frame/test.txt",'w')
file.seek(50)
file.writelines("测试写入1")
file.writelines("测试写入2")
file.writelines("测试写入3")
file.writelines("测试写入4")
file.close()