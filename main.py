from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy = Character("Goblin", 20, 3)
    enemy2 = Character("Big Goblin",30,4)
    enemies = [enemy, enemy2]
    alive = True
    print(hero)
    print(enemy)
    print()

    while hero.is_alive() and any([x.is_alive for x in enemies]):
        if alive == False:
            break
        for enemy in enemies:

            if hero.is_alive:
                hero.attack(enemy)
                print(enemy)
            else:
                alive = False
                break
            if enemy.is_alive():
                enemy.attack(hero)
                print(hero)
            else:
                alive = False
                break
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

if __name__ == "__main__":
    main()
