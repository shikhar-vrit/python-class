cart = [
    ["Bread", 60, 3],
    ["Milk", 120, 4],
    ["Eggs", 15, 10],
]

grand_total = 0
for item in cart:
    name, price, qty = item
    line_total = price * qty
    print(f"{name}: Rs. {line_total}")
    # grand_total = grand_total+line_total
    grand_total += line_total

print(f"Grand total: Rs. {grand_total}")