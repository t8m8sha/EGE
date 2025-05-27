with open('26_4629.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices,reverse=True)
pricescount = len(prices)

shopbigprices = (sum(prices[:pricescount//4])) / 2
radneckaprices = (sum(prices[-pricescount//4:])) / 2

forshopplusprice = sum(prices) - (sum(prices[:pricescount//4])) / 2
forradneckplusprice = sum(prices) - (sum(prices[-pricescount//4:])) / 2





print(forradneckplusprice,forshopplusprice)