## IMPORTS

from ..config import DATABASE_TYPE
from ..heroes import Hero
from ..debug import log
from .mysql import MySQL
from .sqlite import SQLite

## ALL DECLARATION

__all__ = (
    'manager',
    'load_player_data',
    'load_hero_data',
    'save_player_data',
    'save_hero_data',
    )

## DATABASE CHOICE

if DATABASE_TYPE == 1:
    manager = SQLite()
elif DATABASE_TYPE == 2:
    manager = MySQL()
else:
    log(2, 'Cannot load database. Config files states only types 1 or 2.')
    manager = SQLite()
    log(0, 'SQLite has been used by default.')

## SAVING AND LOADING DATA

def load_player_data(player):
    hero = manager.get_player_hero(player)
    if not hero:
        manager.add_player(player)
        manager.connection.commit()
        hero = manager.get_player_hero(player)
    player.hero = Hero.get_subclass_dict()[hero]()

def load_hero_data(player):
    data = manager.get_player_hero_data(player)
    if not data:
        manager.add_hero(player, player.hero)
        manager.connection.commit()
        data = (0, 0)
    player.hero.experience, player.hero.level = data
    for skill in player.hero.skills:
        level = manager.get_player_skill_level(player, player.hero, skill)
        if not level:
            level = 0
        skill.level = level

def save_player_data(player):
    manager.set_player_hero(player)
    manager.set_player_name(player)
    manager.connection.commit()

def save_hero_data(player):
    manager.set_player_hero_data(player, player.hero)
    for skill in player.hero.skills:
        manager.set_player_skill_level(player, player.hero, skill)
    manager.connection.commit()
