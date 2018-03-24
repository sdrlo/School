#Calculate gross pay
#input "Employees Name", "Hours Worked", and "Pay Rate"
#Calculate overtime Overtime = 1.5 * Pay Rate
#Print Employee Name, Gross pay, and if overtime, overtime amount
#Repeat as necessary until user enters sentinel value
#Reference
#https://stackoverflow.com/questions/38469362/payroll-calculator-in-python
#https://www.digitalocean.com/community/tutorials/built-in-python-3-functions-for-working-with-numbers
print("Grantham University Payroll Calculator")
while True:
  Employee = input("Enter your name or '0' to quite: ")
  if Employee == "0":
     print("Good bye!")
     break
  else:
     Hours = (float(input("Enter hours worked: ")))
     Payrate = (float(input("Enter your payrate: $")))
  if Hours <= 40:
     Pay = round(Hours * Payrate, 2)
     print("Employee name: ", Employee)
     print("Gross Pay: $", Pay)
  elif Hours > 40:
     OT = round(Hours - 40.00, 2)
     Pay = round(Hours * Payrate, 2)
     OTRATE = round(Payrate * 1.5, 2)
     OTPAY = round(OT * OTRATE)
     GROSSPAY = round(Pay + OTPAY, 2)
     print("Employee name: ", Employee)
     print("Overtime Pay: $", OTPAY)
     print("Gross Pay: $", GROSSPAY)