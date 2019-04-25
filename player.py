import items, enemies, math


def userinput(prompt, valid):
    s = input(prompt).strip().lower()
    while s not in valid:
        s = input(prompt).strip()
    return s

class Player(object):
    def __init__(self):
        self.weapons = {"dagger" : items.Dagger(), "rock" : items.Rock()}
        self.inventory = {}
        self.magic = {"fire" : items.Fire(), "ice" : items.Ice(), "lightning" : items.Lightning()}
        self.hp = 100
        self.max_hp = 100

    def is_alive(self):
        return self.hp > 0


    def attack(self, enemy):
        print("choose a weapon to attack the {} with".format(enemy.name))
        print("Weapons:")
        for i in self.weapons:
            print(self.weapons[i].name)
        print("or enter 'back' to cancel")
        select = userinput("", list(self.weapons.keys()) + ["back"])
        if select == "back":
            return False
        print("you attack the {} with your {} for {} damage".format(enemy.name, select, self.weapons[select].damage))
        enemy.hp -= self.weapons[select].damage
        return True


    def cast(self, enemy):
        print("choose a spell to use")
        print("Spells:")
        for i in self.magic:
            print(self.magic[i].name)
        print("or enter 'back' to cancel")
        select = userinput("", list(self.magic.keys()) + ["back"])
        if select == "back":
            return False
        print("you cast {} on the {}".format(self.magic[select].name, enemy.name))
        if self.magic[select].type == enemy.weak:
            print("it's super-effective!")
            enemy.hp -= math.floor(2.25 * self.magic[select].damage)
        elif self.magic[select].type == enemy.resist:
            print("it's not very effective")
            enemy.hp -= math.floor(.25 * self.magic[select].damage)
        else:
            enemy.hp -= self.magic[select].damage
        return True





#player = Player()
#enemy = enemies.RedGoblin()
#done = player.attack(enemy)
#print(done)
#print(enemy.hp)
