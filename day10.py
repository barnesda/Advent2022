with open("input/day10.txt") as f:
    input_ = f.read().splitlines()

key_cycles = [20, 60, 100, 140, 180, 220]

cycle = 1
X = 1

signal = []
screen = []
for cmd in input_:
    if cycle in key_cycles:
        signal.append(cycle*X)

    pixel = (cycle - 1) % 40
    diff = pixel - X
    if abs(diff) <= 1:
        screen.append("#")
    else:
        screen.append(".")

    f, n = (cmd[:4], cmd[5:])

    # print(f, n)
    if f == "noop":
        cycle += 1
        continue

    if f == "addx":
        cycle += 1

        if cycle in key_cycles:
            signal.append((cycle)*X)
            # print(cycle, X)

        pixel = (cycle - 1) % 40
        diff = pixel - X
        if abs(diff) <= 1:
            screen.append("#")
        else:
            screen.append(".")

        cycle += 1
        X += int(n)
        continue

# print(signal)
print(sum(signal))

for i in range(0, len(screen), 40):
    print(''.join(screen[i:i+40])) 
