for i in range(20):
    print("*",end=' ')
print()
n=int(input("enter your number of stars "))
for i in range(n):
    print("*",end=' ')
print()
for i in range(4):
    print("x *",end=' ')
print("x")
print()
n=int(input("enter your number of stars and xs "))
for i in range(n//2):
    print("x *",end=' ')
for i in range(n%2):
    print("x")
print()
for i in range(3):
    for i in range(7):
        print("*",end=' ')
    print()
print()
m=int(input("enter your number of rows "))
n=int(input("enter your number of columns"))
for i in range(m):
    for i in range(n):
        print("*",end=' ')
    print()
print()
