yob = int(input("what's your birthday? (year)"))
age = 2018 - yob
print(age)

if age < 10: 
    print("baby")
# if age <18:
#     print("teenager")
# cách này sẽ xuất hiện đồng thời cả baby và teenager
elif age <18:
    print("teenager")
else :
    print("adult")

print("bye bye")