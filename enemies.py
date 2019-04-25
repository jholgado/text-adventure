class Enemy:

    def __init__(self, name, hp, damage, lvl, weak="", resist=""):

        self.name = name
        self.hp = hp
        self.damage = damage
        self.weak = weak
        self.resist = resist
        self.lvl = lvl

    def is_alive(self):
        return self.hp > 0

    def attack(self, player):
        print("The {} attacks for {} damage".format(self.name, self.damage))
        player.hp -= self.damage


class RedGoblin(Enemy):
    def __init__(self, lvl=1):
        super().__init__(name="Red Goblin", hp=10, damage=2, resist="fire", lvl=lvl)


class BlueGoblin(Enemy):
    def __init__(self, lvl=1):
        super().__init__(name="Blue Goblin", hp=10, damage=2, weak="fire", resist="ice", lvl=lvl)


class YellowGoblin(Enemy):
    def __init__(self, lvl=1):
        super().__init__(name="Yellow Goblin", hp=10, damage=2, resist="lightning", lvl=lvl)

