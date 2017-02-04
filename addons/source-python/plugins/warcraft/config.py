## IMPORTS

from paths import PLUGIN_PATH

## CONFIGURATION

LOG_PRIORITY = 0
LOG_LOCATION = PLUGIN_PATH / 'warcraft' / 'debug.log'

DATABASE_TYPE = 1 # Types = 1 (SQLite), 2 (MySQL), 3 (UNKOWN)
SQLITE_LOCATION = PLUGIN_PATH / 'warcraft' / 'database' / 'players.sqlite'
MYSQL_ADDRESS = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_LOGIN = 'username'
MYSQL_PASSWORD = 'password'
MYSQL_DATABASE_NAME = 'warcraft'

WARCRAFT_DEFAULT_HERO = 'Undead'
 
## EXPERIENCE 
BASE_EXPERIENCE = 80
ADDITION_EXPERIENCE = 40
MULTIPLIER_EXPERIENCE = 1.0

KILL_EXPERIENCE = 40
HEADSHOT_EXPERIENCE = 60
ASSIST_EXPERIENCE = 20

SPAWN_EXPERIENCE = 10
MVP_EXPERIENCE = 10
WIN_EXPERIENCE = 20
LOSS_EXPERIENCE = 10

DEFUSE_EXPERIENCE = 20
PLANT_EXPERIENCE = 20

HOSTAGE_PICK_EXPERIENCE = 20
HOSTAGE_RESCUE_EXPERIENCE = 20
