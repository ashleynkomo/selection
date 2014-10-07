#Ashley Nkomo
#07-10-14
#Development Exercise 3

hours = int(input("Please enter the amount of hours worked: "))
hourly_pay = float(input("Please enter your hourly rate of pay: "))

if hours < 0 or hours > 60 :
    print("Invalid number of hours. Please enter hours within the range 0 - 60")

elif hours > 40 :
   extra_hours =  hours - 40
   extra_pay =  hourly_pay * 1.5
   overtime = extra_hours *extra_pay
   regular_pay = 40 * hourly_pay
   total_pay = regular_pay + overtime
   print("Your pay for the hours worked is £{0}".format(total_pay))
else:
    total_pay = hours * hourly_pay
    print("Your pay for the hours worked is £{0}".format(total_pay))

