prices = [78.05, 90.54, 16, 49.99, 150.50, 99.00, 12.10, 456.89, 908.34, 83.05, 652, 6.66]


#A
for i in prices:
    print(f"{i:.02f}".split(".")[0], "рублей", f'{i:.02f}'.split(".")[-1], "копеек", end=" ")

print(id(prices))
#B
print(" ")
print(sorted(prices))
print(id(prices))

#C
reversed_prices = sorted(prices, reverse=True)
print(reversed_prices)
print(id(reversed_prices))

#D
print(reversed_prices[0:5])












