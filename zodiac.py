# # 星座的元组
#
# zodiac_name = (u'魔蝎座', u'水瓶座', u'双鱼座')
# zodiac_days = ((1, 20), (2, 19), (3, 31))
#
# (month, day) = (2, 15)
# zodiac_days = filter(lambda x: x <=(month,day), zodiac_days)
# print(zodiac_days)
# zodiac_len = len(list(zodiac_days)) % 12
# print(zodiac_name[zodiac_len])
a_list = [12, 'xyz']
a_list.append('23')  # 添加到末尾
a_list.remove('xyz')  # 移除元素
print(a_list)
