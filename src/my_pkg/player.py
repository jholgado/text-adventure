import math
from my_pkg import enemies, items


def userinput(prompt, valid):
    s = input(prompt).strip().lower()
    while s not in valid:
        s = input(prompt).strip()
    return s


class Player(object):
    def __init__(self):
        self.weapons = {"rock" : items.Rock()}
        self.magic = {}
        self.m_atk = 2
        self.p_atk = 2
        self.hp = 100
        self.max_hp = 100

    def is_alive(self):
        return self.hp > 0

    def lvl_up(self):
        self.m_atk = math.ceil(1.4 * self.m_atk)
        self.p_atk = math.ceil(1.5 * self.p_atk)
        self.max_hp = math.ceil(1.2 * self.max_hp)
        print("You leveled up!\n")
        print("Max HP: {}".format(self.max_hp))
        print("Physical Attack: {}".format(self.p_atk))
        print("Magic Attack: {}\n".format(self.m_atk))

    def status(self):
        print("Max HP: {}".format(self.max_hp))
        print("Current HP: {}".format(self.hp))
        print("Physical Attack: {}".format(self.p_atk))
        print("Magic Attack: {}\n".format(self.m_atk))

    def attack(self, enemy):
        print("choose a weapon to attack the {} with".format(enemy.name))
        print("Weapons:")
        for i in self.weapons:
            print(self.weapons[i].name)
        print("or enter 'back' to cancel")
        select = userinput("", list(self.weapons.keys()) + ["back"])
        if select == "back":
            return False
        wpn_mult = 1
        if select in enemy.weak:
            print("the {} is weak against {}s".format(enemy.name, select))
            wpn_mult = 2
        enemy.hp -= wpn_mult * (self.p_atk + self.weapons[select].damage)
        print("you attack the {} with your {} for {} damage".format(enemy.name, select, wpn_mult * (self.p_atk + self.weapons[select].damage)))
        return True

    def cast(self, enemy):
        if not self.magic:
            print("you have no spells to use\n")
            return False
        print("choose a spell to use")
        print("Spells:")
        for i in self.magic:
            print(self.magic[i].name)
        print("or enter 'back' to cancel")
        select = userinput("", list(self.magic.keys()) + ["back"])
        if select == "back":
            return False
        print("you cast {} on the {}".format(self.magic[select].name, enemy.name))
        if self.magic[select].element in enemy.weak:
            print("it's super-effective!")
            enemy.hp -= 3 * (self.m_atk + self.magic[select].damage)
            print("the spell deals {} damage".format(3 * (self.m_atk + self.magic[select].damage)))
        else:
            enemy.hp -= self.m_atk + self.magic[select].damage
            print("the spell deals {} damage".format(self.m_atk + self.magic[select].damage))
        return True


if __name__ == '__main__':
    player = Player()
    enemy = enemies.Goblin(color="Grey")
    done = player.attack(enemy)
    print(done)
    print(enemy.hp)
