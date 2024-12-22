from shops import total_bread_price, avarage_bread_price, max_bread_price, max_bread_shops

shops = {
    "Maxi": {
        "Hleb" : 100,
        "Novine" : 50
    },
    "Lidl" : {
        "Hleb" : 90,
        "Novine" : 40
    },
    "Pijaca" : {
        "Hleb" : 70,
        "Novine" : 30
    },
    "Bonik" : {
        "Novine" : 20
    }

}

total_bread_price = 0
total_bread_shops = 0

max_bread_price = 0

for shop_name, items in shops.items():
    if "Hleb" in items:
        total_bread_price += items["Hleb"]
        total_bread_shops += 1

        if max_bread_price < items['Hleb']:
            max_bread_shops = shop_name


average_bread_price = total_bread_price / total_bread_shops


print(average_bread_price)