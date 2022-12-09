with open("input/day6.txt") as f:
    input_ = f.read()

SOP_LENGTH = 4
SOM_LENGTH = 14

found_SOP = False
found_SOM = False

running_unique = 0
last_seen = {}

for idx, l in enumerate(input_, start=1):
    # print(running_unique)
    if l in last_seen:
        running_unique = min(
            idx - last_seen[l], 
            running_unique + 1,
        )
    else:
        running_unique += 1

    last_seen[l] = idx

    if not found_SOP and running_unique == SOP_LENGTH:
        found_SOP = idx

    if not found_SOM and running_unique == SOM_LENGTH:
        found_SOM = idx
        break
        

print(f"Solution 1: {found_SOP}")
print(f"Solution 2: {found_SOM}")
