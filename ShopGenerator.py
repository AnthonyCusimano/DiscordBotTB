from random import randrange
import requests

from discord.ext import commands


#
def DetermineMarkup():
    markupTier = randrange(0, 100)
    if markupTier < 30:
        myMarkUp = 1
    elif markupTier < 50:
        myMarkUp = 1.25
    elif markupTier < 70:
        myMarkUp = 1.5
    elif markupTier < 90:
        myMarkUp = 2.0
    elif markupTier < 95:
        myMarkUp = 0.75

    return myMarkUp


# will create a DnD 5E shop using a score / points system
# TODO blacksmith, general store, provisioner, alchemist, leatherworker
class ShopGenerator(commands.Cog):

    def __init__(self, _debug=False):

        if _debug:
            # trying
            self.myMarkupTier = randrange(0, 100)
            print(self.myMarkupTier)
            if self.myMarkupTier < 30:
                myMarkUp = 1
            elif self.myMarkupTier < 50:
                myMarkUp = 1.25
            elif self.myMarkupTier < 70:
                myMarkUp = 1.5
            elif self.myMarkupTier < 90:
                myMarkUp = 2.0
            elif self.myMarkupTier < 95:
                myMarkupTier = 0.75

            print(self.myMarkupTier)
            item = requests.get("https://www.dnd5eapi.co/api/equipment/")
            for todo_lole in item.json()['results']:
                requester = 'https://www.dnd5eapi.co' + todo_lole['url']
                lole = requests.get(requester)
                coster = (lole.json()['cost']['quantity'])
                costWMarkup = coster * self.myMarkupTier
                currancy = lole.json()['cost']['unit']
                name = lole.json()['name']
                print(name + " costs " + str(costWMarkup) + currancy)

            # shopELO = 0

    #
    @commands.command(name="Blacksmith", aliases=["BS"])
    async def Blacksmith(self, ctx):

        myMarkupTier = DetermineMarkup()
        print(myMarkupTier)

        nextItemOdds = randrange(0, 50)
        nextItemOdds = 25
        if nextItemOdds > 24:
            myMarkupTier
            item = requests.get("https://www.dnd5eapi.co/api/equipment/amulet")  # medium?
            await ctx.channel.send("The Blacksmith has an Amulet in stock, which costs {quan} {Sigurd}".format
                                   (quan=float(item.json()['cost']['quantity']) * myMarkupTier,
                                    Sigurd=item.json()['cost']['unit']))
        item = requests.get("https://www.dnd5eapi.co/api/equipment/ball-bearings-bag-of-1000")  # medium?
        item = requests.get("https://www.dnd5eapi.co/api/equipment/battleaxe")  # likely
        item = requests.get("https://www.dnd5eapi.co/api/equipment/breastplate")  # unlikely
        item = requests.get("https://www.dnd5eapi.co/api/equipment/chain-10-feet")  # very likely
        item = requests.get("https://www.dnd5eapi.co/api/equipment/chest")  # unlikely
        item = requests.get("https://www.dnd5eapi.co/api/equipment/cooks-utensils")  # likely
