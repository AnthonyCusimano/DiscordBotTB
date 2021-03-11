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
            print(todo_lole['name'])
            # T_thisItem = requests.get("https://www.dnd5eapi.co/api/equipment" + todo_lole['url'])
            # print(requests.get("https://www.dnd5eapi.co/api/equipment" + todo_lole['url']))
            # print(T_thisItem.json()['name'])
            # print(T_thisItem['cost']['quantity'])
        # print(item.json()["name"])WORKS with acid arrow
        shopELO = 0

