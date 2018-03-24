#Quick Check Out Program
p1 = float(input("Price of item 1: "))
p2 = float(input("Price of item 2: "))
p3 = float(input("Price of item 3: "))
p4 = float(input("Price of item 4: "))
p5 = float(input("Price of item 5: "))
s = p1 + p2 + p3 + p4 + p5
t = s * 0.06
gt = s + t
print("Sub Total = $", s)
print("Tax = $", int(t * 100) / 100.0)
print("Total = $", gt)