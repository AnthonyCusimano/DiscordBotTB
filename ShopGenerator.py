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
# TODO have argument to ignore out of stock items
def GrabItem(_ctx, _shopName, _url, _minimumStock, _maximumStock, _markup, _odds=0):
    isInStock = randrange(1, 100)

    if _minimumStock != _maximumStock:
        itemStock = randrange(_minimumStock, _maximumStock)
    else:
        itemStock = _minimumStock
    # TODO probably make these global / static
    T_Slang = "{shopName} has an {item} in stock, which costs {quan} {Sigurd}"
    T_SlangPlural = "{shopName} has {count} {item}s in stock, which cost {quan} {Sigurd} each"
    T_SlangNone = "{shopName} has no {item}s in stock"
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
    async def Blacksmith(self, ctx, _shopName="The Blacksmith"):

        T_ShopName = _shopName
        T_MyMarkupTier = DetermineMarkup()

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/crowbar", 1, 8, T_MyMarkupTier, 95))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/amulet", 1, 1, T_MyMarkupTier, 50))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/ball-bearings-bag-of-1000",
            1, 6, T_MyMarkupTier, 50))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/battleaxe", 2, 8, T_MyMarkupTier, 75))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/block-and-tackle", 2, 8, T_MyMarkupTier, 40))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/breastplate", 2, 8, T_MyMarkupTier, 30))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/chain-10-feet", 1, 4, T_MyMarkupTier, 80))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/chest", 1, 2, T_MyMarkupTier, 20))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/cooks-utensils", 2, 6, T_MyMarkupTier, 45))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/crowbar", 1, 9, T_MyMarkupTier, 90))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/dagger", 1, 12, T_MyMarkupTier, 95))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/pick-miners", 2, 4, T_MyMarkupTier, 60))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/pot-iron", 2, 8, T_MyMarkupTier, 95))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/whetstone", 1, 3, T_MyMarkupTier, 96))

    #
    @commands.command(name="Carpenter")
    async def Carpenter(self, ctx, _shopName="The Carpenter"):

        T_ShopName = _shopName
        T_MyMarkupTier = DetermineMarkup()

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/chest", 1, 2, T_MyMarkupTier, 30))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/ladder-10-foot", 1, 1, T_MyMarkupTier, 75))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/barrel", 1, 3, T_MyMarkupTier, 80))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/basket", 2, 4, T_MyMarkupTier, 13))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/bucket", 3, 6, T_MyMarkupTier, 89))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/carpenters-tools", 1, 10, T_MyMarkupTier, 97))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/greatclub", 1, 1, T_MyMarkupTier, 87))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/pole-10-foot", 2, 9, T_MyMarkupTier, 80))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/quarterstaff", 1, 1, T_MyMarkupTier, 80))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/quiver", 1, 2, T_MyMarkupTier, 55))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/shovel", 1, 6, T_MyMarkupTier, 79))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/staff", 1, 1, T_MyMarkupTier, 96))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/torch", 1, 16, T_MyMarkupTier, 99))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/woodcarvers-tools", 1, 2, T_MyMarkupTier, 60))

    #
    @commands.command(name="Leatherworker",aliases=["LW"])
    async def Leatherworker(self, ctx, _shopName = "The Leatherworker"):

        T_ShopName = _shopName
        T_MyMarkupTier = DetermineMarkup()

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/barding-leather", 1, 1, T_MyMarkupTier, 47))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/barding-padded", 1, 1, T_MyMarkupTier, 40))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/barding-studded-leather", 1, 1, T_MyMarkupTier,
            30))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/clothes-travelers", 3, 10, T_MyMarkupTier, 79))

        # TODO maybe have armor tag used
        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/hide", 4, 10, T_MyMarkupTier, 90))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/leather", 4, 10, T_MyMarkupTier, 90))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/barding-leather", 1, 3, T_MyMarkupTier, 70))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/leatherworkers-tools", 3, 6, T_MyMarkupTier,
            95))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/net", 1, 3, T_MyMarkupTier, 60))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/padded", 1, 2, T_MyMarkupTier, 80))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/pouch", 6, 13, T_MyMarkupTier, 99))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/quiver", 1, 4, T_MyMarkupTier, 63))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/robes", 1, 3, T_MyMarkupTier, 61))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/sack", 4, 9, T_MyMarkupTier, 87))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/saddlebags", 4, 9, T_MyMarkupTier, 87))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/sling", 3, 30, T_MyMarkupTier, 99))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/studded-leather", 1, 2, T_MyMarkupTier, 61))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/tent-two-person", 1, 3, T_MyMarkupTier, 40))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/waterskin", 3, 10, T_MyMarkupTier, 99))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/whip", 1, 3, T_MyMarkupTier, 70))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/case-map-or-scroll", 1, 7, T_MyMarkupTier, 82))

    #
    @commands.command(name="ChapelShop", aliases=["CShop"])
    async def ChapelShop(self, ctx, _shopName="The Chapel"):
        T_ShopName = _shopName
        T_MyMarkupTier = DetermineMarkup()

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/holy-water-flask", 1, 64, T_MyMarkupTier, 100))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/backpack", 2, 6, T_MyMarkupTier, 64))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/amulet", 10, 25, T_MyMarkupTier, 100))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/bedroll", 1, 6, T_MyMarkupTier, 82))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/bell", 1, 1, T_MyMarkupTier, 61))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/blanket", 3, 16, T_MyMarkupTier, 99))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/book", 1, 4, T_MyMarkupTier, 50))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/candle", 1, 6, T_MyMarkupTier, 87))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/clothes-common", 1, 6, T_MyMarkupTier, 87))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/donkey", 1, 2, T_MyMarkupTier, 35))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/drum", 1, 1, T_MyMarkupTier, 33))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/dulcimer", 1, 1, T_MyMarkupTier, 33))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/emblem", 8, 17, T_MyMarkupTier, 99))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/healers-kit", 1, 5, T_MyMarkupTier, 80))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/herbalism-kit", 1, 5, T_MyMarkupTier, 80))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/horn", 1, 3, T_MyMarkupTier, 60))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/ink-1-ounce-bottle", 1, 3, T_MyMarkupTier, 87))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/ink-pen", 2, 6, T_MyMarkupTier, 93))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/jug-or-pitcher", 1, 8, T_MyMarkupTier, 76))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/lamp", 1, 3, T_MyMarkupTier, 90))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/lantern-bullseye", 1, 2, T_MyMarkupTier, 64))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/lantern-hooded", 1, 2, T_MyMarkupTier, 64))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/mess-kit", 3, 8, T_MyMarkupTier, 90))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/oil-flask", 2, 7, T_MyMarkupTier, 71))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/paper-one-sheet", 1, 70, T_MyMarkupTier, 90))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/parchment-one-sheet", 1, 70, T_MyMarkupTier, 90))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/pony", 1, 3, T_MyMarkupTier, 68))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/pot-iron", 1, 3, T_MyMarkupTier, 68))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/potion-of-healing", 1, 3, T_MyMarkupTier, 81))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/priests-pack", 1, 6, T_MyMarkupTier, 91))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/rations-1-day", 3, 29, T_MyMarkupTier, 99))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/reliquary", 1, 3, T_MyMarkupTier, 99))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/scholars-pack", 1, 1, T_MyMarkupTier, 87))


    #
    @commands.command(name="Provisioner", aliases=["Provisions"])
    async def Provisioner(self, ctx, _shopName="The Provisioner"):

        T_ShopName = _shopName
        T_MyMarkupTier = DetermineMarkup()

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/rations-1-day", 6, 25, T_MyMarkupTier, 99))

        await ctx.channel.send(GrabItem(
            ctx, T_ShopName, "https://www.dnd5eapi.co/api/equipment/backpack", 1, 3, T_MyMarkupTier, 85))
