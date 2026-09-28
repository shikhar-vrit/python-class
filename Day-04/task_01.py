tasks = []

task = input("Add a task (or 'quit'): ")
while task != "quit":
    tasks.append(task)
    task = input("Add a task (or 'quit'): ")

#tasks = ["Do Homework", "Workout", "cooking", "Running"]

count = 1
for t in tasks:
    print(f"{count}. {t}")
    count += 1

# Remove a task
number = int(input("Enter the task number to remove: "))

removed_task = tasks.pop(number - 1)
# tasks.pop(2)
print(f"Removed: {removed_task}")

# Show remaining tasks
count = 1
for t in tasks:
    print(f"{count}. {t}")
    count += 1




# cart = [
#     ["Bread", 60, 2],
#     ["Milk", 120, 1],
#     ["Eggs", 15, 12],
# ]

# grand_total = 0
# for item in cart:
#     name, price, qty = item
#     line_total = price * qty
#     print(f"{name}: Rs. {line_total}")
#     # grand_total += line_total


# print(f"Grand total: Rs. {grand_total}")








# chart = [
#     ["Empty", "Empty", "Empty", "Empty"],
#     ["Empty", "Empty", "Empty", "Empty"],
#     ["Empty", "Empty", "Empty", "Empty"],
# ]

# name = input("Student name: ")
# row = int(input("Row (0-2): "))
# col = int(input("Column (0-3): "))
# chart[row][col] = name

# for r in chart:
#     print(r)

# # Count empty seats
# empty_seats = 0

# for row in chart:
#     empty_seats += row.count("Empty")

# print(f"Empty seats: {empty_seats}")