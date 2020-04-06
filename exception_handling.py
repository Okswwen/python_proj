# # 捕获事件的异常
#
# try:
# 	year = int(input('input 要输入正整数：'))
# except ValueError:
# 	print('年份要输入数字')


def counter(a=10000):
    def arg(x=0):
        return {"id": a + x, "name": "", "age": ""}

    a += 1
    return arg


num = counter()
print(num())
print(num(1))
