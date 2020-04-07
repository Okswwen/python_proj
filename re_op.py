# 正则表达式

import re

p = re.compile(".{3}")
print(p.match("btb"))

# r 避免转义，使用鸳鸯输出
print(r"\n")

t = re.compile(r"(\d+)-(\d+)-(\d+)")
print(t.match("2018-5-23").group())
matchTime = t.match("2018-5-23").groups()
year, month, day = matchTime
print(year)
print(month)
print(day)

phone = "123-456-789 # 这是电话号码"
p2 = re.sub(r"#.*$", "", phone)
print(p2)
