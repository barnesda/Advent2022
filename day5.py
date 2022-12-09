with open("input/day5_moves.txt") as f:
    input_ = f.read().splitlines()
     
stacks = [
    [],
    ["R","Q","G","P","C","F"][::-1],
    ["P","C","T","W"][::-1],
    ["C","M","P","H","B"][::-1],
    ["R","P","M","S","Q","T","L"][::-1],
    ["N","G","V","Z","J","H","P"][::-1],
    ["J","P","D"][::-1],
    ["R","T","J","F","Z","P","G","L"][::-1],
    ["J","T","P","F","C","H","L","N"][::-1],
    ["W","C","T","H","Q","Z","V","G"][::-1],
]


# re.match(r'move (?P<amt>\d+) from (?P<source>\d+) to (?P<dest>\d+)', line)

from collections import deque

for line in input_:
    n, from_, to_ = line.split(" ")

    n = int(n)
    from_ = int(from_)
    to_ = int(to_)

    # part1
    # for i in range(n):
    #     stacks[to_].append(stacks[from_].pop())
    
    temp = []
    for i in range(n):
        temp.append(stacks[from_].pop())
    
    for i in temp[::-1]:
        stacks[to_].append(i)


print(''.join(s.pop() for s in stacks[1:]))
        
      


     
    
