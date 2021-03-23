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
    else:
        myMarkUp = 0.7

    return myMarkUp


# will create a DnD 5E shop using a score / points system
# if you roll under _odds on a D100 the item is not in stock
# TODO blacksmith, general store, provisioner, alchemist, leatherworker
def GrabItem(_ctx, _shopName, _url, _minimumStock, _maximumStock, _markup, _odds=0):
    isInStock = randrange(1, 100)
    itemStock = randrange(_minimumStock, _maximumStock)
    # TODO probably make these global / static
    T_Slang = "The {shopName} has an {item} in stock, which costs {quan} {Sigurd}"
    T_SlangPlural = "The {shopName} has {count} {item}s in stock, which cost {quan} {Sigurd} each"
    T_SlangNone = "The {shopName} has no {item}s in stock"
    T_Item = requests.get(_url)

    if isInStock > _odds:
        if itemStock > 1:
            return T_SlangPlural.format(shopName=_shopName, count=itemStock, item=T_Item.json()['name'],
                                        quan=float(T_Item.json()['cost']['quantity']) * _markup,
                                        Sigurd=T_Item.json()['cost']['unit'])
        elif itemStock < 1:
            return T_Slang.format(shopName=_shopName,item=T_Item.json()['name'],
                                  quan=float(T_Item.json()['cost']['quantity']) * _markup,
                                  Sigurd=T_Item.json()['cost']['unit'])

    return T_SlangNone.format(shopName=_shopName, item=T_Item.json()['name'])




class ShopGenerator(commands.Cog):

    # _shopName "Blacksmith"
    # DEBUG does not idiotproof _minimumStock or _maximumStock in any way
    # _odds only good for items rarely held by the store

    #
    def __init__(self, _debug=False):

        if _debug:

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
        await ctx.channel.send(GrabItem(
                               ctx, "Blacksmith", "https://www.dnd5eapi.co/api/equipment/crowbar", 1, 8, myMarkupTier))

        # nextItemOdds = randrange(0, 50)
        # nextItemOdds = 25
        # slang = "The Blacksmith has an {item} in stock, which costs {quan} {Sigurd}"
        # slangPlural = "The Blacksmith has {count} {item}s in stock, which cost {quan} {Sigurd} each"
        # if nextItemOdds > 24:
        #     myMarkupTier
        #     item = requests.get("https://www.dnd5eapi.co/api/equipment/amulet")  # medium?
        #     await ctx.channel.send(slang.format
        #                            (item="Amulet", quan=float(item.json()['cost']['quantity']) * myMarkupTier,
        #                            Sigurd=item.json()['cost']['unit']))
        # item = requests.get("https://www.dnd5eapi.co/api/equipment/ball-bearings-bag-of-1000")  # medium?
        # item = requests.get("https://www.dnd5eapi.co/api/equipment/battleaxe")  # likely
        # item = requests.get("https://www.dnd5eapi.co/api/equipment/breastplate")  # unlikely

        # using nextItemOdds to determine number of 10 foot chains
        # nextItemOdds = randrange(0, 4)
        # if nextItemOdds != 0:
        #     item = requests.get("https://www.dnd5eapi.co/api/equipment/chain-10-feet")  # very likely
        # if nextItemOdds == 1:
        #     await ctx.channel.send(slang.format(item="10 foot chain",
        #                                         quan=float(item.json()['cost']['quantity']) *myMarkupTier,
        #                                         Sigurd=item.json()['cost']['unit']))
        # elif nextItemOdds > 1:
        #     await ctx.channel.send(slangPlural.format(item="10 foot chain", count=str(nextItemOdds),
        #                                               quan=float(item.json()['cost']['quantity']) * myMarkupTier,
        #                                               Sigurd=item.json()['cost']['unit']))


        # item = requests.get("https://www.dnd5eapi.co/api/equipment/chest")  # unlikely
        # item = requests.get("https://www.dnd5eapi.co/api/equipment/cooks-utensils")  # likely
        # using nextItemOdds to determine number of crowbars
        # nextItemOdds = randrange(0, 8)
        # if nextItemOdds != 0:
        #     item = requests.get("https://www.dnd5eapi.co/api/equipment/crowbar")  # very likely
        # if nextItemOdds == 1:
        #     await ctx.channel.send(slang.format (item="crowbar",
        #                                         quan=float(item.json()['cost']['quantity']) * myMarkupTier,
        #                                          Sigurd=item.json()['cost']['unit']))
        # elif nextItemOdds > 1:
        #     await ctx.channel.send(slangPlural.format(item="crowbar", count=str(nextItemOdds),
        #                                               quan=float(item.json()['cost']['quantity']) * myMarkupTier,
        #                                               Sigurd=item.json()['cost']['unit']))

        # always has a dagger on hand
        # item = requests.get("https://www.dnd5eapi.co/api/equipment/dagger")
        # nextItemOdds = randrange(1, 12)
        # if nextItemOdds == 1:
        #     await ctx.channel.send(slang.format(item="dagger",
        #                                         quan=float(item.json()['cost']['quantity']) * myMarkupTier,
        #                                         Sigurd=item.json()['cost']['unit']))

        # else:
        #     await ctx.channel.send(slangPlural.format(item="dagger", count=str(nextItemOdds),
        #                                               quan=float(item.json()['cost']['quantity']) * myMarkupTier,
        #                                               Sigurd=item.json()['cost']['unit']))


