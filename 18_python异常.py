#
# try:
#     file = open("D:/log/test_java_frame/test.txt",'w')
#     file.write("ceshi异常1111111111222222222222333333333")
# except IOError:
#     print("文件异常")
# else:
#     print("文件写入成功")
#     file.close()


# try:
#     file = open("D:/log/test_java_frame/test.txt",'w')
#     file.write("ceshi异常1111111111222222222222333333333")
# finally:
#     print("文件异常")

def parseInt(var):
    if int(var) < 10:
        raise Exception("你的输入小于10")

    try:
        return int(var)
    except:
        print("传入字符不是int")

parseInt("0")

