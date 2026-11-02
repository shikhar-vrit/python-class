# users = {"ram": "ram123", "sita": "sita456"}

# # 1. Add yourself
# users["shikhar"] = "shikhar123"

# name = input("Username: ").strip().lower()
# password = input("Password: ")

# # 2. Check empty password
# if password == "":
#     print("Password missing")
# elif name not in users:
#     print("User not found")
# elif users[name] == password:
#     print(f"Welcome, {name.title()}!")
# else:
#     print("Wrong password")






users = {"ram": "ram123", "sita": "sita456"}
users["shikhar"] = "shikhar123"  ## adding

name = input("Username: ").strip().lower()
password = input("Password: ")

if name not in users:
    print("User not found")
elif not password:
    print("missing password")
elif users[name] == password:
    print(f"Welcome, {name.title()}!")
else:
    print("Wrong password")