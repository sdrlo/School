def intro():
  print("High School BMI Calculator")
def get_weight():
  weight = float(input("Enter your weight in pounds: "))
  return weight
def get_height():
  height = float(input("Enter your height in inches: "))
  return height
def calc_bmi():
  bmi = round(weight *703 / (height * height), 2)
  return bmi
def print_result():
  print("Height:", height,"Weight:", weight,"BMI:", bmi, sep="\n")
while True:
  intro()
  Student = input("Enter your name or '0' to quite: ")
  if Student == "0":
    print("Good bye!")
    break
  else:
    height = get_height()
    weight = get_weight()
    bmi = calc_bmi()
    print_result()
