
class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Spell(Item):
    def __init__(self, name, description, value, damage, type):
        self.damage = damage
        self.type = type
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Lightning(Spell):
    def __init__(self):
        super().__init__(name="Lightning",
                         description="Hurl a lightning bolt at the enemy",
                         value=0,
                         damage=5,
                         type="lightning")


class Fire(Spell):
    def __init__(self):
        super().__init__(name="Fire",
                         description="Launch a fire ball at the enemy",
                         value=0,
                         damage=4,
                         type="fire")


class Ice(Spell):
    def __init__(self):
        super().__init__(name="Ice",
                         description="impale the enemy with an ice shard",
                         value=0,
                         damage=7,
                         type="ice")


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
