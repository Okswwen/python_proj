# 将小说的人物书写到txt中

file1 = open('name.txt', mode='w')
file1.write('诸葛亮')
file1.close()

file2 = open('name.txt')
print(file2.read())
file2.close()