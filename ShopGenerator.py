import requests


#
class ShopGenerator:

    def __init__(self):
        item = requests.get("https://www.dnd5eapi.co/api/spells/acid-arrow/")
        # for todo_item in item.json():
        #     print(todo_item["count"])
        print(item.content["name"])
        shopELO = 0

