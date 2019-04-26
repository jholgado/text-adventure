from my_pkg.player import Player, userinput
from my_pkg import level, items


def play():
    print("Welcome to the Tower of Trials")
    print("Do you wish to enter and test your might? (yes/no)")
    select = userinput("", ["yes", "no"])
    if select == "no":
        print("You walk away from the tower and return home")
        return
    i = 1
    weapons = [items.Dagger(), items.Sword(), items.Spear(), items.Axe()]
    magic = [items.Fire(), items.Lightning(), items.Ice()]
    player = Player()
    print("A few things to note before you start:")
    print("enemies have different weaknesses to weapons and magic")
    print("their magic weaknesses will be determined by color (hint: try to match colors)")
    print("their weapon weaknesses are determined by the enemy type")
    print("finally, your power will increase for each floor you climb, but so will that of your enemies\n")
    print("when you are ready to begin, type 'yes'")
    userinput("", ["yes"])
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
    print("Floors Completed: " + str(i-1))

play()
