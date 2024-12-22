from functools import total_ordering

shops = {
    "Maxi": {
        "Hleb": 100,
        "Novine": 50,
    },
    "Idea": {
        "Hleb": 95,
        "Novine" : 40,
    },
    "Lidl": {
        "Hleb": 80,
        "Novine" : 30,
    },
    "Freeshop" :{
        "Novine" : 20,
    },
    "Pijaca" :{
        "Hleb" : 100,
    },
}
total_bread_price = 0
total_bread_shops = 0


max_bread_price = 0
max_bread_shops = ""

for shop_name, items in shops.items():
    if "Hleb" in items:
        total_bread_price += items["Hleb"]
        total_bread_shops += 1

        if max_bread_price < items['Hleb']:
            max_bread_price = items['Hleb']
            max_bread_price_shop = shop_name



avarage_bread_price = total_bread_price / total_bread_shops

print(avarage_bread_price)
print(max_bread_price,max_bread_price_shop)
