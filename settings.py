import configparser
import os

settings = configparser.ConfigParser()
settings._interpolation = configparser.ExtendedInterpolation()
settings.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'resources/settings.ini'))
settings.sections()

WALL = settings.get('GridSymbols', 'WALL')
PACKAGE = settings.get('GridSymbols', 'PACKAGE')
LOAD = settings.get('GridSymbols', 'LOAD')
ESCORT = settings.get('GridSymbols', 'ESCORT')

ROWS_NUMBER = int(settings.get('GridInfo', 'ROWS_NUMBER'))
COLS_NUMBER = int(settings.get('GridInfo', 'COLS_NUMBER'))

ITERATIONS_NUMBER = int(settings.get('RunInfo', 'ITERATIONS_NUMBER'))
ESCORTS_NUMBER = int(settings.get('RunInfo', 'ESCORTS_NUMBER'))
LOADS_NUMBER = int(settings.get('RunInfo', 'LOADS_NUMBER'))