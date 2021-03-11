import requests


# will create a DnD 5E shop using a score / points system
class ShopGenerator:

    def __init__(self):
        # item = requests.get("https://www.dnd5eapi.co/api/spells/acid-arrow/")
        item = requests.get("https://www.dnd5eapi.co/api/equipment/")
        # for todo_item in item:
        #     print(todo_item)
        # print(item.json()['results'])
        for todo_lole in item.json()['results']:
            # print(todo_lole['url']) WORKS
            # print(todo_lole['name'])
            requester = 'https://www.dnd5eapi.co' + todo_lole['url']
            # print(requester)
            lole = requests.get(requester)
            coster = str(lole.json()['cost']['quantity'])
            currancy = lole.json()['cost']['unit']
            name = lole.json()['name']
            print(name + " costs " + coster + currancy)
            # gamerItem = requests.get('https://www.dnd5eapi.co/api/equipment' + todo_lole['url'])
            # print(todo_lole['url'])
            # print(gamerItem['index'])
            # print(gamerItem.json()['weight'])
            # for ape in todo_lole.json()['cost']:
            #     print("lole")
            # todo_lole.json()
            # T_thisItem = requests.get("https://www.dnd5eapi.co/api/equipment" + todo_lole['url'])
            # print(requests.get("https://www.dnd5eapi.co/api/equipment" + todo_lole['url']))
            # print(T_thisItem.json()['name'])
            # print(T_thisItem['cost']['quantity'])
        # print(item.json()["name"])WORKS with acid arrow
        shopELO = 0

