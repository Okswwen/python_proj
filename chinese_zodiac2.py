# 记录生肖，根据输入年份判断生肖

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# year = int(input('请输入年份：'))
# num = year % 12
# print(num)
# print(chinese_zodiac[num])
# if num == 2:
# 	print('狗年走大运')
# for item in chinese_zodiac:
# 	print(item)

for year in range(2000, 2021):
	print('%s：年的生肖是: %s' %(year, chinese_zodiac[year % 12]))

# 在序列中 in 不在序列中 not in
# 字符串拼接 +
# 字符串多次重复 * num num 重复的次数
# 字符串切片 ：[:]

# print('狗' in chinese_zodiac)
# print('狗' not in chinese_zodiac)
# print(chinese_zodiac + chinese_zodiac)
# print('abc' * 3)