# 定义类


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def run_role(self):
        print("%s : %s " % (self.name, self.hp))


class Monster:
    "定义某些monster"
    pass


user1 = Player("tom", 100)
user2 = Player("jerry", 200)
user1.run_role()
