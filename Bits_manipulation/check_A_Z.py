# check the presence of char a-z in the word
lowerchar = 0
upperchar = 0
word = input("Enter word:")
for c in word:
    if c.islower():
        diff = ord(c) - ord("a")
        checker = 1 << diff
        lowerchar = lowerchar | checker
    else:
        diff = ord(c) - ord("A")
        checker = 1 << diff
        upperchar = upperchar | checker

if lowerchar == ((1 << 26) - 1) and upperchar == ((1 << 26) - 1):
    print("yes")
else:
    print("no")
