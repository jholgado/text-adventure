
class Item(object):
    # The base class for all items (originally intended for more than just weapons and spells)
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "{}\n=====\n{}\n".format(self.name, self.description)


class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)

    def __str__(self):
        return "{}\n=====\n{}\nDamage: {}".format(self.name, self.description, self.damage)


class Spell(Item):
    def __init__(self, name, description, damage, element):
        self.damage = damage
        self.element = element
        super().__init__(name, description)

    def __str__(self):
        return "{}\n=====\n{}\nDamage: {}".format(self.name, self.description, self.damage)


class Lightning(Spell):
    def __init__(self):
        super().__init__(name="Lightning",
                         description="Hurl a lightning bolt at the enemy",
                         damage=15,
                         element="yellow")


class Fire(Spell):
    def __init__(self):
        super().__init__(name="Fire",
                         description="Launch a fire ball at the enemy",
                         damage=14,
                         element="red")


class Ice(Spell):
    def __init__(self):
        super().__init__(name="Ice",
                         description="impale the enemy with an ice shard",
                         damage=12,
                         element="blue")


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning",
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small rusty dagger",
                         damage=10)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A sturdy steel sword",
                         damage=15)


class Spear(Weapon):
    def __init__(self):
        super().__init__(name="Spear",
                         description="A long wooden shaft with a steel pointed blade on one end",
                         damage=15)


class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Axe",
                         description="A short wooden shaft with a broad double headed blade",
                         damage=15)




