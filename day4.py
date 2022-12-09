with open("input/day4.txt") as f:
    inp = f.read().splitlines()

sol1 = 0
sol2 = 0
for line in inp:
     l, r = line.split(",")
     # print(l, r)

     l1, l2 = l.split("-")
     r1, r2 = r.split("-")

     l1 = int(l1)
     l2 = int(l2)
     r1 = int(r1)
     r2 = int(r2)

     # l contained within r
     if l1 >= r1 and l2 <= r2:
         sol1 += 1
         sol2 += 1
     # r contained within l
     elif l1 <= r1 and l2 >= r2:
         sol1 += 1
         sol2 += 1
     # Other overlap
     elif (r1 <= l1 <= r2 or r1 <= l2 <= r2 or
          l1 <= r1 <= l2 or l1 <= r2 <= l2):
         sol2 += 1

     
    
print(sol1)
print(sol2)
