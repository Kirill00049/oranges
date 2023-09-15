import requests

headers = {"Content-Type":"application/json", "token": "64fb4ccc14fd064fb4ccc14fd3"}
getScore = "https://datsorange.devteam.games/info"
getLatestNews = "https://datsorange.devteam.games/news/LatestNews"
getLatest5MinNews = "https://datsorange.devteam.games/news/LatestNews5Minutes"
getLatest1MinNews = "https://datsorange.devteam.games/news/LatestNews1Minute"
getStockSell = "https://datsorange.devteam.games/sellStock"
getStockBuy = "https://datsorange.devteam.games/buyStock"
getStockAll = "https://datsorange.devteam.games/getSymbols"
bestBuy = "https://datsorange.devteam.games/BestPriceBuy"
removeBid = "https://datsorange.devteam.games/RemoveBid"
limitPriceBuy = "https://datsorange.devteam.games/LimitPriceBuy"
limitPriceSell = "https://datsorange.devteam.games/LimitPriceSell"

allSymbols = {}

buyBestPrice = {"symbolId": 7, "quantity": 10}

removeBid = {"bidId": 16}

response = requests.get(getStockAll, headers=headers)
print(response.json())

# Словарик
for i in response.json():
    allSymbols.update({i["ticker"][8:]: i["id"]})
print(allSymbols)

response1 = requests.get(getStockSell, headers=headers)


dict_for_buy = []

# Закупаем

# for i in response1.json():
#     if i["bids"]:
#         for elem in i["bids"]:
#             if elem["price"] <=80:
#                 limitBuy = {"symbolId": i["id"], "price": 80, "quantity": 5}
#                 response = requests.post(limitPriceBuy, headers=headers, json=limitBuy)
#                 break
#                 print(response.json())
#                 dict_for_buy.append([i["id"], elem["price"], elem["quantity"]])
# print(dict_for_buy)

# Проверем цены
response2 = requests.get(getStockBuy, headers=headers)
for item in response2.json():
    if item["id"] == 119:
        print(item)

#Продаем

response3 = requests.post(limitPriceSell, headers=headers, json={
"symbolId": 119,
"price": 99,
"quantity": 8})
