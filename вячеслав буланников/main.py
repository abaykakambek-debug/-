"""Запуск Dungeon Code — урок 3. Команда, предметы и босс."""
from heroes import Warrior, Mage, Rogue, Archer
from items import Weapon, Potion
from boss import Boss
from battle import team_battle


def main():
    warrior = Warrior("Артур")
    mage = Mage("Луна")
    rogue = Rogue("Тень")
    archer = Archer("Элрин")
    team = [warrior, mage, rogue, archer]

    warrior.inventory.add_item(Weapon("Стальной меч", 8))
    warrior.inventory.add_item(Potion("Малое зелье", 20))
    mage.inventory.add_item(Potion("Зелье здоровья", 40))
    rogue.inventory.add_item(Weapon("Кинжал", 5))
    archer.inventory.add_item(Weapon("Эльфийский лук", 10))
    archer.inventory.add_item(Potion("Эликсир леса", 50))

    print("\n🧙 НАША КОМАНДА")
    for hero in team:
        print(hero)
        hero.inventory.show()

    training_dummy = Boss("Тренировочный голем")
    training_dummy.hp = 100
    warrior.attack(training_dummy)

    boss = Boss("Огненный дракон")
    team_battle(team, boss)


if __name__ == "__main__":
    main()
