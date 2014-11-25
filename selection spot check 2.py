#Ashley Nkomo
#09-10-14
#Question 2 Spot Check

FirstName = input("Please enter your first name: ")
LastName = input("Please enter your last name: ")
Gender = input("Please enter your gender: ")

if Gender == "male":
    print("Mr {0} {1}".format(FirstName, LastName))
elif Gender == "female":
    print("Ms {0} {1}".format(FirstName, LastName))
else:
    print("Please enter an appropriate gender")
