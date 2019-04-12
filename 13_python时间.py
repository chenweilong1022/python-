import time

print(time.time())

print(dir(time))
print(time.localtime())
print(time.gmtime())
print(time.time_ns())
# print(time.clock())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

import calendar

cal = calendar.month(2019, 4)
print("以下输出2016年1月份的日历:")

print(cal)

