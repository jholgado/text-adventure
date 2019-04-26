from my_pkg.player import Player
from my_pkg import level, items


def play():
    i = 1
    weapons = [items.Dagger(), items.Sword(), items.Spear(), items.Axe()]
    magic = [items.Fire(), items.Lightning(), items.Ice()]
    player = Player()
    while player.is_alive():

        current_lvl = level.Level(i)
        print("you enter floor " + str(i))
        current_lvl.battle(player)
        if player.is_alive():
            print("Floor " + str(i) + " cleared!\n")
            player.lvl_up()
            player.hp = player.max_hp
            if 1 <= i <= 4:
                print("You received a {}\n".format(weapons[i - 1].name))
                player.weapons[weapons[i - 1].name.lower()] = weapons[i - 1]
            if 3 <= i <= 5:
                print("You received a {} spell\n".format(magic[i - 3].name))
                player.magic[magic[i - 3].name.lower()] = magic[i - 3]
            i += 1
    print("YOU DIED")


play()
