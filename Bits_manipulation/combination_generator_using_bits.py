# J ABISHEK AML - A ENGINEERING
string = input("enter the word:")
n = len(string)
for i in range(1, 1 << n):
    for shift in range(0, n):
        if i & (1 << shift):
            print(string[shift], end="")
    print()
