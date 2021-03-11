import requests


# will create a DnD 5E shop using a score / points system
class ShopGenerator:

    def __init__(self):
        item = requests.get("https://www.dnd5eapi.co/api/equipment/")
        for todo_lole in item.json()['results']:
            requester = 'https://www.dnd5eapi.co' + todo_lole['url']
            lole = requests.get(requester)
            coster = str(lole.json()['cost']['quantity'])
            currancy = lole.json()['cost']['unit']
            name = lole.json()['name']
            print(name + " costs " + coster + currancy)

        shopELO = 0

