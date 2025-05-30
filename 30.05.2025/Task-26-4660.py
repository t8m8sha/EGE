with open('26_4660 (1).txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]
prices = sorted(prices)
pricescount = len(prices)

shoptags = sum(prices) - sum(prices[:N//4]) / 2

radneckprices = sorted(prices,reverse=True)
radnecktags = sum(radneckprices) - sum(radneckprices[3::4]) / 2

print(radnecktags,shoptags)


