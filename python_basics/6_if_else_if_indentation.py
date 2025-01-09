i = 10   # i is initialized
if i<5:  # condition is applied
    print("i is greater than 5")
else:
    print("i is less than or equal to 5")


#Adding elif (Else if)
j = 20
if j>20:
    print("j is greater than 20")
elif j>10:
    print("j is greater than 10 but less than or equal to 20")
else:
    print("j is 10 or less")

#using logical operators - and, or, not
k = 15
if k>10 and k<20:
    print("k is between 10 and 20")
else:
    print("k is not in the range")

# Nested if statements
l = 8
if l>5:
    if l%2 == 0:
        print(" l is greater than 5 and even number")
    else:
        print(" l is greater than 5 and odd")
else:
    print(" l is 5 or less")

#if else with User Input
age = int(input("Enter your age: "))
if age >=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#Short-Hand if and if-else
#you can use short versions of if and if-else when there is only statement to execute
i = 5
if i>3: print("s is greater than 3")

j = 10
print("Even") if j%2 == 0 else print("Odd")
