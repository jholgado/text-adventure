from player import Player
import level
import random

def play():
    i = 1
    player = Player()
    while player.is_alive():

        current_lvl = level.Level(i)
        for j in range(i):
            current_lvl.battle(player)
            if not player.is_alive():
                break
        if player.is_alive():
            print("Floor " + str(i) + " cleared!\n")
            i += 1
    print("YOU DIED")


play()
