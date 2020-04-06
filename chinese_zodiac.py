# 记录生肖，根据输入年份判断生肖

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
# chinese_zodiac[4]
# print(chinese_zodiac[0:4])

year = 2018
num = year % 12
print(num)
print(chinese_zodiac[num])

# 在序列中 in 不在序列中 not in
# 字符串拼接 +
# 字符串多次重复 * num num 重复的次数
# 字符串切片 ：[:]

print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)
print(chinese_zodiac + chinese_zodiac)
print('abc' * 3)