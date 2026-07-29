roll_no = int(input("enter students roll number:"))
name = input("enter students name:")
marks_1 = int(input("enter the marks in first subject:"))
marks_2 = int(input("enter the marks in second subject:"))
marks_3 = int(input("enter the marks in third subject:"))
total = marks_1 + marks_2 + marks_3
print("total Marks:",total)
percentage = total/3
print("Percentage Obtained:",percentage)
if(percentage>=60):
    print("Division = First")
elif(percentage>=50):
    print("Division = Second")
elif(percentage>=40):
    print("Division = Third")
else:
    print("Division = Fail")