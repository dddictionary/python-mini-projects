import math
import unittest
#^^^needed for math.gcd (greatest common divisor) to reduce fraction

###----------------------------------------------------------------
### Complete the Fraction class here
###----------------------------------------------------------------


class Fraction:
    def __init__(self, num, den):
        gcd = math.gcd(num, den) * (-1 if den < 0 else 1)
        self.num = num // gcd
        self.den = den // gcd

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_den = self.den * other.den
        new_num = (self.num * other.den) + (other.num * self.den)
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_den = self.den * other.den
        new_num = (self.num * other.den) - (other.num * self.den)
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Fraction(self.num * other.den, self.den * other.num)

    def __gt__(self, other):
        if self.num / self.den > other.num / other.den:
            return True
        return False
      
    def __lt__(self, other):
        if self.num / self.den < other.num / other.den:
            return True
        return False

    def __eq__(self, other):
        if self.num / self.den == other.num / other.den:
            return True
        return False


###----------------------------------------------------------------
### Write your test code below
###----------------------------------------------------------------
#Test code for Problem 1
print("Checking str and simplification")
print("+" + "-" * 25 + "+")
f = Fraction(4, 6)
print(f.__str__())
#should print: 2/3
g = Fraction(18, 30)
print(g)
#should print: 3/5
h = Fraction(7, 8)
print(h)
#should print: 7/8
print("\n")

print("Checking Addition")
print("+" + "-" * 25 + "+")
a = f.__add__(g)  #adding 2/3 and 3/5
print(a)
#should print: 19/15
b = f + h
print(b)
#should print: 37/24
c = Fraction(3, 8) + Fraction(1, 8)
print(c)
#should print: 1/2
print("\n")

print("Checking Subtraction")
print("+" + "-" * 25 + "+")
a = f.__sub__(g)  #adding 2/3 and 3/5
print(a)
#should print: 19/15
b = f - h
print(b)
#should print: 37/24
c = Fraction(3, 8) - Fraction(1, 8)
print(c)
#should print: 1/2
print("\n")

print("Checking Multiplication")
print("+" + "-" * 25 + "+")
a = f.__mul__(g)  #adding 2/3 and 3/5
print(a)
#should print: 19/15
b = f * h
print(b)
#should print: 37/24
c = Fraction(3, 8) * Fraction(1, 8)
print(c)
#should print: 1/2
print("\n")

#Test code for Problem 2 - continued from Problem 1
print("Checking Division")
print("+" + "-" * 25 + "+")
a = f.__truediv__(g)  #adding 2/3 and 3/5
print(a)
#should print: 19/15
b = f / h
print(b)
#should print: 37/24
c = Fraction(3, 8) / Fraction(1, 8)
print(c)
#should print: 1/2
print("\n")


print("Checking >,<,=")
print("+" + "-" * 25 + "+")
#Test code for Problem 4 - continued from Problem 1
d = f.__gt__(g) 
print(f"{f} > {g}? {f>g}") #should print: 2/3 3/5 True
print("5/6 > -3/2?", Fraction(5,6) < Fraction(-3,2)) # should return False
print("-3/2 == -3/2?", Fraction(-3,2) == Fraction(-3,2)) # should return False

print("\n")

print("Checking Negagive Fractions")
print("+" + "-" * 25 + "+")

print(Fraction(-10,-16))
print(Fraction(-5,16))
print(Fraction(32,-16))
print("\n")

print("Printing sixteenths subtraction chart")

# list1 = []
# e = 0
# h = Fraction(1,16)
# while e < 16:
#   list1.append(str(Fraction(1,16) + Fraction(e,1)*h))
#   e += 1

# print(list1)

list = []
for i in range(16):
  list.append(Fraction(i, 16))

list2 = []
hrow = " "
for i in range(16):
  hrow += str(list[i]) + " "*(8-len(str(list[i])))
# print("+" + "-" * len(hrow)+ "+")
# print(hrow)
# print("+" + "-" * len(hrow)+ "+")

i,j = 0,0
for i in range(16):
  j = 1
  vrow = " "
  vrow += str(list[i]) + " "*(8-len(str(list[i]))) 
  #print(vrow) 
  for j in range(16):
    sub = list[j].__sub__(list[i])
    vrow += str(sub) + " "*(8-len(str(sub)))
    j += 1
  #print(vrow)  
  i += 1
  # print(i)

