"""
Arithmetic - Add, Sub, Mult, Div, Modulus, Exponentiation, FloorDivision
Assignment -   =, +=, -=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=
Comparison -   ==, !=, <, >, <=, >=
Logical -   and, or, not
Identity - is, is not
Membership - in, not in
Bitwise  -   &, |, ^, ~, <<, >>
"""

#Exponentiation - to the power of and it is represented by **
a = 3
b = 2
print(a ** b)

#FloorDivision - when you divide, it will ignore the digits after the decimal
c = 5
d = 2
print(c//d)

a+=b #this means a is = a+b
print(a)

print(a := 100) # you are assigning this value of as the latest value
print(a)
e = 100
print(a + e)

#comparison
print( b := 100) #this is the latest value of b
print(a == b)
print(a != b)
print (a <= b)
print (a >= b)

#logical
print(a<=b and b<=a)
print(not(a<b))

#identity
print(a is b)
print(a is not b)
print(not(a is not b))

#Precedence
"""
() - Parantheses
** - Exponentation
+a, -a, ~a
*, / , //, %
+, -
<<, >>
&
^
|
comparison, identity, membership
not
and
or
"""
i = 10
j = 20
k = 30
print((j-i) ** (k-j) - 200 + 300 * 10)