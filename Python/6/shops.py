

# Svaka prodavnica ima svoje ime, svaka prodavnica ima svoje proizvode i njihove cene

shops = {
    "Maxi": {
        "Hleb" : 100,
        "Novine" : 50,
    },
    "Idea" :{
        "Hleb" : 95,
        "Novine" : 62,
    },
    "Lidl" : {
        "Hleb" : 89,
        "Novine" : 45,
    },
    "Roda" : {
        "Hleb" : 93,
        "Novine" : 41,
    },
    "Free shop" : {
        "Novine" : 41,
    },

}

# Napisati petlju koja ce ispisati sve cene hleba

total_bread_price = 0
total_bread_shops = 0

max_bread_price = 0

for shop_name, items in shops.items():
    if "Hleb" in items:
        total_bread_price += items['Hleb']
        total_bread_shops += 1
        if max_bread_price < items['Hleb']:
             max_bread_price = items['Hleb']
             max_bread_price_shop = shop_name

total_shops = len(shops)


avarage_bread_price = total_bread_price / total_shops



print(avarage_bread_price)
print(max_bread_price, max_bread_price_shop)