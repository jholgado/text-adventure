import random
from my_pkg import enemies
from my_pkg.player import userinput


class Level(object):
    def __init__(self, lvl):
        self.lvl = lvl
        self.enemyList = [enemies.Goblin("Blue", lvl), enemies.Goblin("Red", lvl), enemies.Goblin("Yellow", lvl)]

    def battle(self, plyr):
        enemy = random.choice(self.enemyList)
        print("a {} has appeared\n".format(enemy.name))
        while plyr.is_alive() and enemy.is_alive():
            done = False
            while not done:
                print("Player: {} hp".format(plyr.hp))
                print("{}: {} hp\n".format(enemy.name, enemy.hp))
                action = userinput("enter action: \nattack \nmagic \nstatus\n", {"attack", "magic", "status"})
                if action == "attack":
                    done = plyr.attack(enemy)
                elif action == "magic":
                    done = plyr.cast(enemy)
                elif action == "status":
                    plyr.status()

            if not enemy.is_alive():
                print("the {} dies\n".format(enemy.name))
            else:
                enemy.attack(plyr)



#curr_lvl = Level(1)
#player = player.Player()
#curr_lvl.battle(player)
