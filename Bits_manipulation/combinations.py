n = int(input("Enter the number of vehicles"))
v = []
ways = 0
for i in range(n):
    v.append(int(input("Enter the vehicle occupancy:")))
member = int(input("Enter the number of members:"))
for ctr in range(1, 1 << n):
    currtot = 0
    for shift in range(0, n):
        if ctr & (1 << shift):
            currtot += v[shift]
    if currtot == member:
        ways += 1
print(ways)
# i donno the sum
