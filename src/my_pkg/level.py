import random
from my_pkg import enemies, player
from my_pkg.player import userinput


class Level(object):
    def __init__(self, lvl):
        self.lvl = lvl
        if lvl >= 3:
            self.enemyList = [enemies.Goblin("Grey", lvl), enemies.Goblin("Blue", lvl), enemies.Goblin("Red", lvl), enemies.Goblin("Yellow", lvl),
                              enemies. Ogre("Grey", lvl), enemies.Ogre("Blue", lvl), enemies.Ogre("Red", lvl), enemies.Ogre("Yellow", lvl)]
        else:
            self.enemyList = [enemies.Goblin("Grey", lvl), enemies.Goblin("Blue", lvl), enemies.Goblin("Red", lvl), enemies.Goblin("Yellow", lvl)]

    def battle(self, plyr):   #logic for flow of battle encounter
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


if __name__ == '__main__':
    curr_lvl = Level(1)
    player = player.Player()
    curr_lvl.battle(player)
