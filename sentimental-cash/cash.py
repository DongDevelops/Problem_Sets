from cs50 import get_float
# TODO
while True:
    change = get_float("How much change is owed? ")
    if change > 0:
        print(f"Change owed: {change}")
        break

count = 0

while change >= 0.25:
    change = change - 0.25
    count += 1


while change >= 0.10:
    change = change - 0.10
    count += 1


while change >= 0.05:
    change = change - 0.05
    count += 1


while change >= 0.01:
    change = change - 0.01
    count += 1


print(f"{count} ")
