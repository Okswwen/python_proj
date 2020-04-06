# 定义类


# class Player:
#     def __init__(self, name, hp):
# 			self.name = name
# 			self.hp = hp
#
# 		def run_role(self):
# 			print("%s : %s " % (self.name, self.hp))
#
# user1 = Player("tom", 100)
# user2 = Player("jerry", 200)
# user1.run_role()

# 类的继承
class Monster:
    "定义某些monster"

    def __init__(self, hp):
        self.hp = hp

    def run(self):
        print("移动")


class Animals(Monster):
    "普通怪物"

    def __init__(self, hp=10):
        super().__init__(hp)


a2 = Animals(1)
print(a2.run())


class Boss(Monster):
    "普通怪物"
    pass
