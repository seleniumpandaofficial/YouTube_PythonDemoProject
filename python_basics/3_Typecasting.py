#Converting a datatype into another
#Integer to Float
number = 5
print(type(number))
converted = float(number)
print(type(converted))
print(converted)

#Float to Integer
floatingnumber= 1.9
print(type(floatingnumber))
converted1 = int(floatingnumber)
print(converted1)


#String to Integer
age = "21" # age is a str
print(type(age))
numberchange = int(age) #str to convert to int
print(type(numberchange))
print(numberchange)
print(numberchange + 21)

#Integer to String
i = 10
grade = str(i)
print(type(grade))
print(grade)
# print(grade + 10) #this proves that grade is a str now

#String to Float
lastname = "1.5"
print(type(lastname))
decimalnumber = float(lastname)
print(type(decimalnumber))
print(decimalnumber + 1.5)

#Float to String
height = 6.2
howhigh = str(height)
print(type(howhigh)) #str
print(howhigh + "tall enough")


#List to Tuple
my_list = [1,2,3]
converted = tuple(my_list)
print(converted)

#Tuple to List
my_tuple = (4,5,6)
converted = list(my_tuple)
print(converted)

#String to List
text = "Hello"
converted = list(text)
print(converted)

#List to Set
my_list = [1,2,3,3,3,4,4]
converted = set(my_list)
print(converted)

#Integer to Boolean
num = 0
converted = bool(num)
print(converted)

num1 = 1
converted1 = bool(num1)
print(converted1)

#String to Boolean
text = ""
converted = bool(text)
print(converted)

text1 = "Hello"
converted1 = bool(text1)
print(converted1)


#String to Integer - special
i = "John"
print(type(i))
convert = int(i)
print(convert)













