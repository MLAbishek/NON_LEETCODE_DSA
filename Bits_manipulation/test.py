s = input("Enter string:")
uppercase = 0
lowercase = 0
for c in s:
    if c.islower():
        diff = ord(c) - ord("a")
        lowercase |= 1 << diff
    else:
        diff = ord(c) - ord("A")
        uppercase |= 1 << diff
if lowercase == (1 << 26) - 1 and uppercase == (1 << 26) - 1:
    print("YES")
else:
    print("NO")
