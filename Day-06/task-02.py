prices = {"tea": 20, "coffee": 50, "samosa": 25}
prices["momo"] = 150
print("Menu:", prices)

item = input("What do you want? ")
qty  = int(input("How many? "))

price = prices.get(item, 0)
print("Price of one:", price)
print("Total bill  :", price * qty)

print(f"Cheapest price: {min(prices.values())}")
print(f"costliest price: {max(prices.values())}")

print(f"sorted name: {sorted(prices)}")
print(f"sorted name: {sorted(prices.items())}")