with open("input/day1.txt") as f:
    food_list = f.read()

totals = [0]
for cal in food_list.split("\n"):
    cal = cal.strip()

    if not cal:
        totals.append(0)
        continue

    totals[-1] += int(cal)


# print(totals)
print(f"max: {max(totals)}")

totals.sort(reverse=True)
print(f"Top 3: {totals[0:3]}, sum: {sum(totals[0:3])}")



# 2nd pass, now with list comprehensions
by_elf = food_list.split("\n\n")
totals = [
    sum(
        int(calorie or 0) 
        for calorie in elf.split("\n")
    ) 
    for elf in by_elf
]
totals.sort(reverse=True)

print(f"max: {max(totals)}")
print(f"Top 3: {totals[0:3]}, sum: {sum(totals[0:3])}")
