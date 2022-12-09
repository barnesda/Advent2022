with open("input/day3.txt") as f:
    rs = f.read().splitlines()

shared = []

sacks = []
badges = []
for idx, ruck in enumerate(rs, start=1):
    # print("new sack")
    pivot = len(ruck)//2

    l = ruck[:pivot]
    r = ruck[pivot:]

    for item in l:
        if item in r:
            shared.append(item)
            break

    if not idx % 3:
        for item in ruck:
            if item in sacks[-1] and item in sacks[-2]:
                badges.append(item)
                # print(f"badge {item}")
                break

    sacks.append(ruck)

total1 = 0
for item in shared:
    if 'a' <= item <= 'z':
        total1 += (ord(item) - ord('a')) + 1
    elif 'A' <= item <= 'Z':
        total1 += (ord(item) - ord('A')) + 27

print("pt1", total1)

total2 = 0
for item in badges:
    if 'a' <= item <= 'z':
        total2 += (ord(item) - ord('a')) + 1
    elif 'A' <= item <= 'Z':
        total2 += (ord(item) - ord('A')) + 27

print("pt2", total2)
