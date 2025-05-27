with open('26_4660.txt') as file:
    N = int(file.readline())
    prices = [int(tag)for tag in file]

prices = sorted(prices,reverse=True)
pricecount = len(prices)

bigtags = prices[:pricecount//4]
smalltags = prices[-pricecount//4:]

radneck = sum(prices) - sum(prices[3::4]) / 2
mananger = sum(prices) - sum(prices[-N//4:]) / 2

print(radneck,mananger)
