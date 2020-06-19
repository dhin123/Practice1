import cmath

a = int(input("Enter real numbers"))
b= int(input("Enter real numbers"))
c = int(input("Enter real numbers"))

d = b* b/-4*a*c

sol1 = -b + cmath.sqrt(d)/2*a
sol2 = -b - cmath.sqrt(d)/2*a
print("The roots are", sol1, sol2)

