from random import randrange
from random import choice

from discord.ext import commands


#
with open("OneShot.txt") as o:
    shotLines = o.readLines()
shotOne = shotLines[0].split(',')
shotTwo = shotLines[1].split(',')
shotOne[-1] = shotOne[-1][:-1]

#
def FormOneShot():
    ""