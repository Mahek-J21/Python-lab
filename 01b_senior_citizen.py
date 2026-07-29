from datetime import date
persons_name = input("Enter the persons name:")
persons_dob = int(input("Enter the persons year of birth:"))
Cur_year = date.today().year
persons_age = Cur_year - persons_dob
if(persons_age>60):
    print(persons_name, "aged", persons_age,"Years is a senior citizen")
else:
    print(persons_name,"aged",persons_age,"Years is not a senior citizen")