import requests


#
class ShopGenerator:

    def __init__(self):
        # item = requests.get("https://www.dnd5eapi.co/api/spells/acid-arrow/")
        item = requests.get("https://www.dnd5eapi.co/api/equipment/")
        # for todo_item in item:
        #     print(todo_item)
        # print(item.json()['results'])
        for todo_lole in item.json()['results']:
            print(todo_lole['name'])
        # print(item.json()["name"])WORKS with acid arrow
        shopELO = 0

