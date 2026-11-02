# def add(a, b):
#     return a + b

# print(add(2, 3))

# add_two = lambda a, b: a + b

# print(add_two(2, 4))


# greet = lambda name, msg="Hello": f"{msg}, {name}!"

# print(greet("Ram", "Namaste"))


# total = lambda *nums: sum(nums)
# total = lambda *nums: max(nums)

# print(total(10, 20, 30))

# check = lambda m=0: "Pass" if m >= 40 else "Fail"
# print(check(60))


# square = lambda n: n * n

# print(square(3))


add = lambda a, b: a + b
shout = lambda word: word.upper() + "!"
is_even = lambda n: n % 2 == 0
bigger = lambda a, b: a if a > b else b

# print(add(2, 3))
# print(add("momo", "tea"))
# # print(shout("namaste"))
# print(is_even(7))
# print(bigger(10, 25))
# print(add(5))


# words = ["banana", "kiwi", "apple", "fig", "ab"]

# print(sorted(words, key=len))

# print(sorted(words, key=lambda word: word[-1]))


# words = ["banana", "kiwi", "apple", "fig"]
# last = lambda w: w[-1]

# for word in words:
#     print(word, "->", last(word))

# print(sorted(words, key=last))


# students = [("Ram", 92), ("Sita", 78), ("Hari", 65)]

# print(sorted(students))

# print(sorted(students, key=lambda student: student[1], reverse=True))

# top = max(students, key=lambda s: s[1])
# low = min(students, key=lambda s: s[1])

# print(top)    
# print(low)

# name, score = top
# print(f"{name} score {score}")


# students = [
#     {"name": "Ram", "marks": 92},
#     {"name": "Sita", "marks": 78},
# ]
# best = max(students, key=lambda student: student["marks"])
# print(best)
# print(type(best))
# print(best["marks"])


# menu = {"momo": 150, "tea": 30, "lassi": 80}
# cheap_first = sorted(menu.items(), key=lambda item: item[1], reverse=True)
# print(cheap_first)


words = ["Python", "is", "very", "fun"]
nums = [-7, 3, -1, 5]
team = [("Ram", 21), ("Sita", 19), ("Hari", 25)]

# print(sorted(words, key=lambda w: len(w)))
# print(sorted(words, key=len))
# print(sorted(nums, key=lambda n: abs(n)))
# print(max(team, key=lambda p: p[1]))
# print(min(team, key=lambda person: person[1])[0])  # ("Sita", 19)
# print(sorted(words, key=lambda w: w.lower()))
# print(sorted(words))



# prices = [100, 250, 80]
# print(prices)
# new_prices = []
# for p in prices:
#     new_prices.append(p + 20)
# print(new_prices)


# new_prices = list(map(lambda p: p + 20, prices))
# print(new_prices) 



# marks = "67 45 92".split()
# print(marks)                    
# print(list(map(int, marks)))


# names = ["ram", "sita", "hari"]
# print(list(map(lambda n: n.upper(), names)))


# def square(n):
#     return n * n

# print(list(map(square, [1, 2, 3])))


nums = [1, 2, 3]
result = list(map(lambda n: n * 10, nums))

# print(result)
# print(result)

# print(list(result))
# print(list(result))


# tens = list(map(lambda n: n * 10, nums))
# print(tens, sum(tens))



marks = [67, 35, 92, 28, 54]

# passed = []
# for m in marks:
#     if m >= 40:
#         passed.append(m)
# print(passed)


# passed = list(filter(lambda m: m >= 40, marks))
# print(passed)

# words = ["momo", "tea", "chowmein", "dal", "ab"]
# print(list(filter(lambda w: len(w) > 3, words)))



# marks = [67, 35, 92, 28, 54]

# bonus = map(lambda m: m + 5, marks)
# passed = filter(lambda m: m >= 40, bonus)
# # bonus = map(lambda m: m + 5, passed)
# final = list(passed)

# print(final)          # [72, 97, 59]
# print(sum(final))     # 228
# print(max(final))

# print(list(map(lambda m: m + 5, filter(lambda m: m >= 60, marks))))



nums = [1, 2, 3, 4, 5]
names = ["ram", "sita", "gopi"]

# print(list(map(lambda n: n * n, nums)))
# print(list(filter(lambda n: n > 3, nums)))

# print(list(map(len, names)))

print(list(map(lambda n: n.upper(), names)))
print(list(filter(lambda n: "a" in n, names)))
print(list(map(lambda n: n + 1, nums)))