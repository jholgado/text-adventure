import enemies, player, random
from player import userinput

class Level(object):
    def __init__(self, lvl):
        self.lvl = lvl
        self.enemyList = [enemies.BlueGoblin(lvl), enemies.RedGoblin(lvl), enemies.YellowGoblin(lvl)]

    def battle(self, plyr):
        enemy = random.choice(self.enemyList)
        print("a {} has appeared\n".format(enemy.name))
        while plyr.is_alive() and enemy.is_alive():
            done = False
            while not done:

                print("{}: {} hp".format(enemy.name, enemy.hp))
                action = userinput("enter action: \nattack \nmagic \ninventory\n", {"attack", "magic", "inventory"})
                if action == "attack":
                    done = plyr.attack(enemy)
                elif action == "magic":
                    done = plyr.cast(enemy)
                #elif action == "inventory":



            if not enemy.is_alive():
                print("the {} dies\n".format(enemy.name))
            else:
                enemy.attack(plyr)
            print("Player: {}/{} hp".format(plyr.hp, plyr.max_hp))
            print("{}: {} hp".format(enemy.name, enemy.hp))

        if not plyr.is_alive():
            print("YOU DIED\n")


#curr_lvl = Level(1)
#player = player.Player()
#curr_lvl.battle(player)
