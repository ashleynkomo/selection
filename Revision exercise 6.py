#Ashley Nkomo
#30-09-14
#Revision Exercise 4

number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter a second number: "))
number3 = float(input("Please enter a third number: "))

if number3 > number1 and number2:
    print("The  number entered is larger")
elif number2 > number1 and number3 :
    print("The second number entered is larger")
elif number1 > number2 and number3:
    print("The third number entered is larger")
    
else:
    print("The numbers are exactly the same")
    
