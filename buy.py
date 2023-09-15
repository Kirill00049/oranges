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

# Закупаем
response = requests.get(getStockAll, headers=headers)
response1 = requests.get(getStockSell, headers=headers)

dict_for_buy = []

for i in response1.json():
    if i["bids"]:
        for elem in i["bids"]:
            if elem["price"] <=100:
                #limitBuy = {"symbolId": i["id"], "price": 80, "quantity": 5}
                #response = requests.post(limitPriceBuy, headers=headers, json=limitBuy)
                #break
                dict_for_buy.append([i["id"], elem["price"], elem["quantity"]])
print(dict_for_buy)