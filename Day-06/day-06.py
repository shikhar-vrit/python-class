# d1 = dict(name="ram", age=25, address="KTM")

# print(type(d1))
# print(d1)

# d2 = dict([("abc", 6), ("xyz", 7)])
# print(type(d2))
# print(d2)


# ok = {1: "one", "two": 2, (3, 4): "tuple key", 1.5: "float"}
# print(type(ok))
# print(ok)

# info = {"marks": [70, 80], "pass": True}
# print(type(info))
# print(info)

# print({"a": 1, "b": 2} == {"b": 2, "a": 1})


# dict1 = {"name": "Hari", "age": 20, "address": "KTM", 0: "zero"}

# print(dict1["age"])
# # print(dict1["phone"])
# print(dict1.get("phone"))
# print(dict1.get("phone", "N/A"))

# print(dict1[0])



## adding and updating

# student = {"name": "Gita", "age": 20}

# student["address"] = "BKT"
# # print(student)
# student["name"] = "Sita"
# # print(student)

# student.update({"phone": "9812345678", "class": 12, "age": 18})
# print(student)

# class1 = student.pop("class")
# print(class1)
# print(student)

# print(student.pop("class", "not found"))

# last_item = student.popitem()
# print(last_item)
# print(student)

# del student["age"]
# print(student)

# student.clear()
# print(student)

# del student
# print(student)



# d = {"a": 1, "b": 2}
# d["c"] = 3
# d["a"] = 10

# print(d)
# print(len(d))
# print(d.get("z", 0))
# print(d.pop("b"))
# print(d)

# print(d["z"])
# print(d.get("z"))


# prices = {"tea": 20, "coffee": 50, "milk": 30}

# print(prices.keys())
# print(prices.values())
# print(prices.items())

# print(list(prices))
# print(list(prices.values()))

# print("tea" in prices)
# print(50 in prices)
# print(50 in prices.values())


# print(len(prices.values()))

# print(sum(prices.values()))




# a = {"tea": 20, "milk": 30}
# b = {"milk": 35, "juice": 60}

# # print(a | b)

# # print({**a, **b})


# a |= b
# print(a)

# print(b)


# s  = {"name": "Ram"}

# print(s.setdefault("age", 20))
# print(s)
# print(s.setdefault("name", "Hari"))
# print(s)

# marks = dict.fromkeys(["math", "science", "english"], 0)
# print(marks)
# marks = dict.fromkeys(["math", "science", "english"])


# names = ["Ram", "Sita", "Hari"]
# marks = [85, 92, 78]


# dict1 = dict(zip(names, marks))
# print(dict1)



# s = {"name": "hari", "age": 20}

# s2 = s
# s2["grade"] = "A"
# print(s2)

# s3 = s.copy()
# s3["address"] = "KTM"
# print(s3)

# s4 = dict(s)
# s4["phone"] = "9812345678"
# print(s4)
# print(s)




# school = {
#     "ram":  {"age": 20, "city": "Pokhara"},
#     "sita": {"age": 19, "city": "Kathmandu"}
# }

# print(school["ram"])
# print(school["sita"]["age"])

# school["ram"]["city"] = "Butwal"
# print(school["ram"])

# school["gita"] ={"age": 22, "city": "Bhaktapur"}
# print(school)





# p = {"pen": 10, "book": 50}
# q = {"book": 60, "bag": 500}

# print("pen" in p.values())
# print(50 in p.values())
# print(list(p.keys()))
# print(p | q)
# print(sum(q.values()))

# r = p.copy()
# r["pen"] = 15
# print(p["pen"])

# print(p.items()[0])