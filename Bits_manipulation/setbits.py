n = int(input("Enter number:"))
setbit = 0
while n > 0:
    setbit += n & 1
    n = n >> 1
print(setbit)
