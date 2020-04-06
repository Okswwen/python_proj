# 时间库
import time


def timer(func):
    def wrapper():
        start_time = time.time()
        print("开始时间：%s" % start_time)
        print("函数运行中...")
        func()
        stop_time = time.time()
        print("结束时间：%s" % stop_time)
        print("time_run 函数运行的时间：%s" % (stop_time - start_time))

    return wrapper


@timer
def time_run():
    time.sleep(3)


time_run()

# print('函数运行中...')
# start_time = time.time()
# print("开始时间：%s" % start_time)
# print("函数运行中...")
# time_run()
# stop_time = time.time()
# print("结束时间：%s" % stop_time)
# print("time_run函数运行的时间：%s" % (stop_time - start_time))
