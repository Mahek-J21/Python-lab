num=input("enter a number:")
print("The number entered is:",num)
uniqDig=set(num)
for element in uniqDig:
    print(element,"occurs",num.count(element),"times")
    