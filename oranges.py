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