contacts = {"Ram": "9801111111", "Sita": "9802222222"}

name = input("New contact name: ")
phone = input("Phone number: ")
contacts[name] = phone
# contacts["Ram"] = 9812345678

print("All contacts:", contacts)
print("Total:", len(contacts))

find = input("Search a name: ")
print("Number:", contacts.get(find, "Not found"))

# Remove one contact
remove_name = input("Contact to remove (name): ")
removed = contacts.pop(remove_name, "Not found")
print("Removed:", removed)

# Print only names
print("Names:", list(contacts.keys()))





# prices = {"tea": 20, "coffee": 50, "samosa": 25}
# prices["momo"] = 150  ### adding momo
# print("Menu:", prices)

# # item = input("What do you want? \n")
# # qty  = int(input("How many? \n"))

# # price = prices.get(item, 0)
# # print("Price of one:", price)
# # print("Total bill  :", price * qty)

# print(f"Cheapest price is: {min(prices.values())}")  ## printing cheapest 
# print(f"costliest price is: {max(prices.values())}")  ## printing costliest

# print(f"Names: {sorted(prices)}")  ## srted names 
# print(f"New menu: {sorted(prices.items())}")  ## sorted menu

