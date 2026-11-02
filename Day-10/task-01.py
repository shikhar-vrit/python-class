text = input("Enter marks with spaces: ")    # 67 45 92 78
marks = []
for part in text.split():
    marks.append(int(part))

print(f"Students: {len(marks)}")
print(f"Highest:  {max(marks)}")
print(f"Lowest:   {min(marks)}")
print(f"Total:    {sum(marks)}")
print(f"Average:  {round(sum(marks) / len(marks), 2)}")
print(f"Sorted:   {sorted(marks, reverse=True)}")

pass_count = 0
passed = []

for m in marks:
    if m > 40:
        pass_count += 1
        passed.append(True)
    else:
        passed.append(False)

print(f"{pass_count} passed.")
if all(passed):
    print("Everone passed!")
# Your job:
# 1. print how many passed (40 or more)
# 2. if all() of them passed, print "Everyone passed!"