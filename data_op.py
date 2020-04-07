# 时间日期库的练习

import datetime
import time

t1 = time.time()
print(t1)
print(time.localtime())
nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
print(nowTime)

d = datetime.datetime.now()
print(d)
