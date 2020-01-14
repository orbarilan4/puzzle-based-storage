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
ITERATIONS_NUMBER = settings.get('GridSymbols', 'ITERATIONS_NUMBER')