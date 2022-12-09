from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property

with open("input/day7.txt") as f:
    input_ = f.read().splitlines()

# Need to keep track of heirarchy
# - Name
# - dir or file
# - contains if dir, size if file
# Need to be able to calculate size recursizely (or keep track of dir sizes too?)

SOL1_MAXSIZE = 100_000
TOTAL_SPACE = 70_000_000
SOL2_NEEDED = 30_000_000

# Globals
state = 'READ_CMD' # or 'STORE_LS'
cache = []

sol1 = 0

@dataclass
class Folder:
    up: Folder | None

    name: str
    contents: dict[str, Folder | File]

    def cd(self, name: str):
        if name == '..':
            return self.up
        else:
            return self.contents[name]

    def process_ls(self, lines: list[str]):
        for l in lines:
            if l[:3] == "dir":
                name = l[4:]
                self.contents[name] = Folder(
                    up = self,
                    name = name,
                    contents = {},
                )
            else:
                size, name = l.split(' ')
                self.contents[name] = File(
                    name=name,
                    size=int(size),
                )
    
    @property
    def size(self) -> int:
        #print(f"checking size of {self}")
        return sum(t.size for t in self.contents.values())
        

@dataclass
class File:
    name: str
    size: int

root = Folder(
    up=None,
    name='/',
    contents={},
)

for line in input_:
    if line == '$ cd /':
        curr = root
        continue

    if state == 'STORE_LS':
        if line[0] != '$':
            cache.append(line)
            continue
        
        curr.process_ls(cache)
        state = 'READ_CMD'
        cache = []

    if line[:4] == '$ cd':
        curr = curr.cd(line[5:])
        continue

    if line[:4] == '$ ls':
        state = 'STORE_LS'
        continue

# I messed up and forgot to check for `ls`s at the end at first
# , so I solved the first part and then didn't understand
#  why the second part *wasn't working*

# I spent like an hour finding that .-.
if state == 'STORE_LS':
    curr.process_ls(cache)
    state = 'READ_CMD'
    cache = []

def sol1_size(node: Folder):
    return sum(d.size for d in all_subdirs(node) if d.size <= SOL1_MAXSIZE)

def sol2_size(node: Folder, needed: int):
    return min(d.size for d in all_subdirs(node) if d.size >= needed)

def all_subdirs(node: Folder) -> list[Folder]:
    all_ = [node]
    if all(isinstance(c, File) for c in node.contents.values()):
        return all_

    for n in node.contents.values():
         if isinstance(n, Folder):
            all_ += all_subdirs(n)
    
    return all_


    
print(sol1_size(root))
print(needed := SOL2_NEEDED-TOTAL_SPACE+root.size)
print(sol2_size(root, needed))
# print(root)



    

