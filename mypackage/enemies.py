


class Enemy:
    def __init__(self, name, hp, damage, color, lvl):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.color = color

    def is_alive(self):
        return self.hp > 0


class BlueGoblin(Enemy):
    def __init__(self):
        super().__init__(name="Blue Goblin", hp=10, damage=2, color="blue")


class RedGoblin(Enemy):
    def __init__(self):
        super().__init__(name="Red Goblin", hp=10, damage=2, color="red")


class YellowGoblin(Enemy):
    def __init__(self):
        super().__init__(name="Yellow Goblin", hp=10, damage=2, color="Yellow")
