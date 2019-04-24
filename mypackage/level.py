import enemies, player

class Level(object):
    def __init__(self, lvl):
        self.lvl = lvl
        self.enemyList = {enemies.BlueGoblin(), enemies.RedGoblin(), enemies.YellowGoblin()}


    def battle(self, plyr, enemy):


