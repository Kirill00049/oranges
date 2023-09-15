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

# Проверем цены
response2 = requests.get(getStockBuy, headers=headers)
for item in response2.json():
    if item["id"] == 101:
        print(item)
    if item["id"] == 498:
        print(item)