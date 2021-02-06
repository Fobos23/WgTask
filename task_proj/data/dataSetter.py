from task_proj.data.taskObjects import ship
from task_proj.data.taskObjects import weapon
from task_proj.data.taskObjects import hull
from task_proj.data.taskObjects import engine
from random import randint


def get_ships():
    ships = []

    i = 1
    while i <= 200:
        new_ship = ship.Ship(f'ship-{i}', f'weapon-{randint(1, 20)}', f'hull-{randint(1, 5)}', f'engine-{randint(1, 6)}')
        ships.append(new_ship)
        i += 1

    return ships


def get_weapons():
    weapons = []

    i = 1
    while i <= 20:
        new_weapon = weapon.Weapon(f'weapon-{i}', randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
        weapons.append(new_weapon)
        i += 1

    return weapons


def get_hulls():
    hulls = []

    i = 1
    while i <= 5:
        new_hull = hull.Hull(f'hull-{i}', randint(1, 20), randint(1, 20), randint(1, 20))
        hulls.append(new_hull)
        i += 1

    return hulls


def get_engines():
    engines = []

    i = 1
    while i <= 5:
        new_engine = engine.Engine(f'engine-{i}', randint(1, 20), randint(1, 20))
        engines.append(new_engine)
        i += 1

    return engines
