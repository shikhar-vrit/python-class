# cart = ["bread", "milk", "egg"]

# print(cart)
# print(cart[2])
# print(cart[-2])

# print(len(cart))

# number = [24, 43, 65, 12, 10, 50]

# # print(number[1:4])
# # print(number[1:5:3])
# print(number[::2])
# print(number[::-1])



fruits = ["apple", "banana", "cherry"]
# print(fruits)
# fruits[1] = "mango"
# print(fruits)
# fruits[0:0] = ["kiwi", "grape"]
# print(fruits)
# fruits[0:2] = ["kiwi", "grape"]
# print(fruits)

# fruits.append("mango")
# print(fruits)
# fruits.insert(1, "kiwi")
# print(fruits)
# fruits.remove("cherry")
# print(fruits)
# print(fruits)
# # last = fruits.pop(1)
# # print(last)
# # print(fruits)

# print("apple" in fruits)

# fruits.clear()
# print(fruits)
# print("apple" in fruits)


scores = [88, 45, 72, 90, 60, 95, 88, 75, 68, 88]
# print(scores)
# print(len(scores))
# print(sum(scores))
# print(max(scores))
# print(min(scores))
# scores.sort()  #
# print(scores)

# print(scores.count(88))
# print(scores)
# print(scores.index(68))
# scores.sort(reverse=True)
# print(scores)


# names = ["Maya", "abel", "Zoe"]
# names.sort()
# print(names)
# names.sort(key=str.lower)
# print(names)




grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(grid[0])
# print(grid[2][1])

# for row in grid:
    # print(row)

# for i in range(2, 10, 2):
#     print(i)


line = "apple,banana,cherry"

fruits = line.split(",")
# print(fruits)

words = "my name is ram".split()
# print(words)

joined = " ".join(words)
# print(joined)

list1 = [10, 20 , 25, 30, 33]
print(f"ltst1: {list1}")

list2 = list1

list2.append(55)
print(f"list2: {list2}")
print(f"list1 new: {list1}")

list3 = [10, 20 , 25, 30, 33]
print(f"list3: {list3}")
list4 = list3.copy()
list4.append(65)
print(f"list4: {list4}")
print(f"list3 new: {list3}")

