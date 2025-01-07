#Python has several categories in terms of data types
# numeric
 #int - whole numbers
 #float - decimal numbers
 #complex - which has a real and imaginary part
age = 25
print(age)
#how will I prove that age is an int
print(type(age)) # this will prove age is what kind of a data type

height = 6.4
print(type(height))

a = 3 + 4j
print(type(a))


# sequence
 #str - a sequence of characters
 #list - ordered collection (modifiable)
 #tuple - ordered collection (immutable - cannot modify)
 #range - represent a sequence of characters

name = "John Hancock"
print(type(name))

name1 = 'Panda Club'
print(type(name1))

cars = ["Mercedes", "Toyota", "BMW"]
print(type(cars))

coordinates = (10, 20)
print(type(coordinates))

numbers = range(5)
print(type(numbers))
print(list(numbers))

numbers1 = range(10)
print(type(numbers1))
print(list(numbers1))



# mapping
 #dict - represents a collection of key-value pairs where keys are unique
student = {"name":"Tom", "age": 11, "grade":6}
print(type(student))

# set
 #set - an unordered collection of unique items
 #frozenset - immutable version of set
unique_numbers = {1,2,3,4,5}
print(type(unique_numbers))

strict_numbers = frozenset([1,2,3,4,5])
print(type(strict_numbers))


# boolean
 #bool - True or False
python_automation_is_easy = True
print(type(python_automation_is_easy))

is_adult = age > 18
print(type(is_adult))

comparing_something = 1>2
print(type(comparing_something))
print(comparing_something)

#binary (home work
 #bytes
 #bytearray
 #memoryview

#NoneType
result = None
print(type(result))

