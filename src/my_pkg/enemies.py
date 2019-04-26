import math

class Enemy: #basic enemy class

    def __init__(self, name, hp, damage, lvl, weak=[], resist=[]):

        self.name = name
        self.hp = math.ceil((lvl * 1.3) * hp)           #hp determines how many hits enemy can take
        self.damage = math.ceil((lvl * 1.3) * damage)   #determines amount of damage dealt in battle
        self.weak = weak                                #list of weapon/magic type weaknesses
        self.lvl = lvl

    def is_alive(self):
        return self.hp > 0

    def attack(self, player):
        print("The {} attacks for {} damage".format(self.name, self.damage))
        player.hp -= self.damage

#enemy types determining weapon weaknesses


class Goblin(Enemy):
    def __init__(self, color="", lvl=1):
        super().__init__(name=color+" Goblin", hp=10, damage=2, weak=["sword", color.lower()], lvl=lvl)


class Ogre(Enemy):
    def __init__(self, color="", lvl=1):
        super().__init__(name=color+" Ogre", hp=25, damage=8, weak=["spear", color.lower()], lvl=lvl)



