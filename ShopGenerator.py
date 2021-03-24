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

    if _minimumStock != _maximumStock:
        itemStock = randrange(_minimumStock, _maximumStock)
    else:
        itemStock = _minimumStock
    # TODO probably make these global / static
    T_Slang = "The {shopName} has an {item} in stock, which costs {quan} {Sigurd}"
    T_SlangPlural = "The {shopName} has {count} {item}s in stock, which cost {quan} {Sigurd} each"
    T_SlangNone = "The {shopName} has no {item}s in stock"
    T_Item = requests.get(_url)

    if isInStock <= _odds:
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

        ShopName = "Blacksmith"

        myMarkupTier = DetermineMarkup()

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/crowbar", 1, 8, myMarkupTier, 95))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/amulet", 1, 1, myMarkupTier, 50))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/ball-bearings-bag-of-1000", 1, 6, myMarkupTier, 50))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/battleaxe", 2, 8, myMarkupTier, 75))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/breastplate", 2, 8, myMarkupTier, 30))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/chain-10-feet", 1, 4, myMarkupTier, 80))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/chest", 1, 2, myMarkupTier, 20))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/cooks-utensils", 2, 6, myMarkupTier, 45))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/crowbar", 1, 9, myMarkupTier, 90))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/dagger", 1, 12, myMarkupTier, 95))

        await ctx.channel.send(GrabItem(
            ctx, ShopName, "https://www.dnd5eapi.co/api/equipment/pot-iron", 2, 8, myMarkupTier, 95))

