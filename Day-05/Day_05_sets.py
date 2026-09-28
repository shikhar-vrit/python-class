# number = {1, 2, 3, 4, 4, 5, 5, 6}
# print(number)

# print(set([1, 1, 2, 3, 4, 4]))

# lst = []
# tup = ()
# set1 = set()



# set1 = {1, 3, 2, 4, 5, 5, 6, 7, (2, 3, 4), [5, 6, 8, 10]}

# print(set1)


# colors = {"red", "blue"}

# colors.add("green")              # add one item
# print(colors)
# colors.add("red")                # already there: no change
# colors.update(["pink", "gold"])  # add many items
# print(colors)

# colors.remove("pink")     # remove (error if missing)
# print(colors)
# colors.discard("black")   # remove (never an error)
# print(colors)
# removed = colors.pop()              # remove a random item
# print(removed)
# colors.clear()            # empty it: set()
# print(colors)
# del colors
# print(colors)




# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6, 7}

# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)
# print(set2 - set1)

# print(set1 ^ set2)


# set1 &= set2
# print(set1)





# small = {1, 2}
# big   = {1, 2, 3, 4}

# print(small >= big)            # True   subset
# print(big.issubset(small))     # True
# print(big >= small)            # True   superset
# print(big.issuperset(small))   # True

# print(small.isdisjoint(big))   # True
# print({1, 2} == {2, 1}) 


# a = {1, 2, 3}
# b = a
# b.add(4)
# print(b)
# print(a)
# c = a.copy()
# c.add(5)
# print(c)
# print(a)



# f = frozenset([1, 2])
# f.add(3)


# list1 = ["ram", "sita", "hari", "krishna", "hari"]
# print(list1)

# set1 = set(list1)
# print(set1)


s = {3, 1, 3, 2, 1}
print(len(s))

s.add(4)
print(sorted(s))

print({1, 2} & {2, 3})
print({1, 2} | {2, 3})

s.discard(9)