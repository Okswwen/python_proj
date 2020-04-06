# 多线程的问题
import threading


def myThread(arg1, arg2):
    print("%s %s" % (arg1, arg2))


for i in range(1, 10000, 1):
    # t = myThread(i, i + 1)
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()
