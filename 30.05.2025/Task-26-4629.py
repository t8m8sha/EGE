with open('26_4629.txt') as file:
    N = int(file.readline())
    prices = [int(tag)for tag in file]
prices = sorted(prices,reverse=True)
pricecount = len(prices)

shopprices = (sum(prices[:pricecount // 4])) / 2
radneckprices = (sum(prices[-pricecount // 4:])) / 2

platashop = sum(prices) - shopprices
plataradneck = sum(prices) - radneckprices

print(plataradneck,platashop)