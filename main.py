import random

print("-- Fret for Freedom --")
print(" ")
print("You were touring North Korea, and you're now held captive in a concentration camp. You're going to be executed soon, so you need to break free.")
print(" ")

health = 100
money = 0
item = []

while True:
    print("Health:", health)
    print("Money:", money)
    print("Inventory:", item, "\n")

    action = input("What would you like to do? (type O for options)\n").lower()

    if action == "o":
        print("\nType E to explore, R to rest, B to bribe, F to fight, and O to bring this panel back up.\n")

    elif action == "e":
        print("You wander around the prison grounds.")
        found_items = ["rope", "knife", "helmet", "chestplate", "leggings", "left boot", "right boot" "shield"]
        found = random.choice(found_items + [None])
        if found:
            item.append(found)
            print(f"You found a {found}!")
        else:
            print("You didn't find anything this time.\n")

    elif action == "r":
        print("You take a short break to rest and recover some health.\n")
        health += 10
        if health > 100:
            health = 100

    elif action == "b":
        print("You use some of your money to bribe a guard for information.")
        money -= 10
        if money < 0:
            print("You don't have enough money to bribe.\n")

    elif action == "f":
        print("You try to fight your way out\n")
        health -= 20
        if health <= 0:
            print("You instantly got shot by one of the guards. Lmao")
            break

    else:
        print("Invalid action.\n")

    if "rope" in item and "knife" in item and money >= 50:
        print("You have everything you need to escape! Congratulations!\n")
        break

print("Thanks for playing!\nIf you enjoyed my game, please like and comment on the repl! This is my first console game and I would love to hear feedback!")
