from math import log10

with open("input/day8.txt") as f:
    inp = f.read().splitlines()

COLOR_RESET = '\033[0m'
VIS_COLOR_MAP = {
    1: '\033[31m', # Red
    0: '\033[32m', # Green
}

SCORE_COLOR_MAP = {
        0: '\033[30m',  # dark gray
        1: '\033[32m',  # green
        2: '\033[34m',  # blue
        3: '\033[35m',  # purple
        4: '\033[33m',  # orange
        5: '\033[31m',  # red
        6: '\033[36m',  # cyan
}


treemap = []
for line in inp:
    treemap.append([int(z) for z in line])

X_sz = len(treemap[0])
Y_sz = len(treemap)

vis_map = [[0 for _ in range(X_sz)] for _ in range(Y_sz)]
score_map = [[0 for _ in range(X_sz)] for _ in range(Y_sz)]
for y in range(Y_sz):
    for x in range(X_sz):
        h = treemap[y][x]
       
        if x in (0, X_sz-1) or y in (0, Y_sz-1) \
        or h > max(treemap[y][:x]) or h > max(treemap[y][x+1:]) \
        or h > max(treemap[i][x] for i in range(0,y)) or h > max(treemap[i][x] for i in range(y+1,Y_sz)):
           vis_map[y][x] = 1

        ss = {}
        for off in range(1, X_sz):
            if x == 0:
                ss['l'] = 0
                break
            elif x-off == 0 or treemap[y][x-off] >= h:
                ss['l'] = off
                break

        for off in range(1, X_sz):
            if x == X_sz-1:
                ss['r'] = 0
                break
            elif x+off == X_sz-1 or treemap[y][x+off] >= h:
                ss['r'] = off
                break

        for off in range(1, Y_sz):
            if y == 0:
                ss['u'] = 0
                break
            elif y-off == 0 or treemap[y-off][x] >= h:
                ss['u'] = off
                break

        for off in range(1, Y_sz):
            if y == Y_sz-1:
                ss['d'] = 0
                break
            elif y+off == Y_sz-1 or treemap[y+off][x] >= h:
                ss['d'] = off
                break

        score_map[y][x] = ss['l'] * ss['r'] * ss['u'] * ss['d'] 

for y in range(Y_sz):
    print(''.join(VIS_COLOR_MAP[v] + str(v) + COLOR_RESET for v in vis_map[y]))

for y in range(Y_sz):
    print(''.join(SCORE_COLOR_MAP[int(log10(s)) if s else 0] + str(int(log10(s)) if s else 0) + COLOR_RESET for s in score_map[y]))

print(sum(sum(v for v in row) for row in vis_map))
print(max(max(s for s in row) for row in score_map))

