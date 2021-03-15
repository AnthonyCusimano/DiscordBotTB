from random import randrange
import requests

from discord.ext import commands


# will create a DnD 5E shop using a score / points system
# TODO blacksmith, general store, provisioner, alchemist, leatherworker
class ShopGenerator:

    def __init__(self, _debug=False):

        if _debug:
            # trying
            myMarkupTier = randrange(0, 100)
            print(myMarkupTier)
            if myMarkupTier < 30:
                myMarkUp = 1
            elif myMarkupTier < 50:
                myMarkUp = 1.25
            elif myMarkupTier < 70:
                myMarkUp = 1.5
            elif myMarkupTier < 90:
                myMarkUp = 2.0
            elif myMarkupTier < 95:
                myMarkupTier = 0.75

            print(myMarkUp)

            item = requests.get("https://www.dnd5eapi.co/api/equipment/")
            for todo_lole in item.json()['results']:
                requester = 'https://www.dnd5eapi.co' + todo_lole['url']
                lole = requests.get(requester)
                coster = (lole.json()['cost']['quantity'])
                costWMarkup = coster * myMarkUp
                currancy = lole.json()['cost']['unit']
                name = lole.json()['name']
                print(name + " costs " + str(costWMarkup) + currancy)

            # shopELO = 0

    #
    @commands.command(name="Blacksmith", aliases=["BS"])
    async def Blacksmith(self, ctx):
        item = requests.get("https://www.dnd5eapi.co/api/equipment/amulet")  # medium?
        item = requests.get("https://www.dnd5eapi.co/api/equipment/ball-bearings-bag-of-1000")  # medium?
        item = requests.get("https://www.dnd5eapi.co/api/equipment/battleaxe")  # likely
        item = requests.get("https://www.dnd5eapi.co/api/equipment/breastplate")  # unlikely
        item = requests.get("https://www.dnd5eapi.co/api/equipment/chain-10-feet")  # very likely
        item = requests.get("https://www.dnd5eapi.co/api/equipment/chest")  # unlikely
        item = requests.get("https://www.dnd5eapi.co/api/equipment/cooks-utensils")  # likely
