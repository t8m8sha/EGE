with open('26_4684.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

pricesshop = sorted(prices)
pricecount = len(prices)

shoptags = sum(pricesshop) - sum(pricesshop[3::6]) / 2

radneckprices = sorted(prices,reverse=True)
radnecktags = sum(pricesshop) - (sum(radneckprices[3::6])) / 2

print(shoptags,radnecktags)