import numpy as np

with open("input/day9.txt") as f:
    inp = f.read().splitlines()

    
head = np.array([0, 0])
tail = np.array([0, 0])

long_rope = [np.array([0, 0]) for _ in range(10)]

D_MAP = {
    'U': np.array([0, 1]),
    'D': np.array([0, -1]),
    'L': np.array([-1, 0]),
    'R': np.array([1, 0]),
}

visited1 = {(0, 0)}
visited2 = {(0, 0)}
for line in inp:
    d, n = line.split(" ")

    n = int(n)

    for s in range(n):
        # pt1
        head += D_MAP[d]
        diff = head - tail

        if diff @ diff > 2:
            tail += np.sign(diff)

        visited1.add(tuple(tail))

        # pt2
        long_rope[0] += D_MAP[d]
        for lead, lag in zip(long_rope, long_rope[1:]):
            diff = lead - lag

            if diff @ diff > 2:
                lag += np.sign(diff)

        visited2.add(tuple(long_rope[-1]))


print(len(visited1))
print(len(visited2))
