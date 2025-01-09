#concatenation - joining two or more Strings, lists or some sequence ( + operator)

#String concatentation - [ + ,  join() ]
Str1 = "Hello"
Str2 = "World"
result = Str1 + " " + Str2
print(result)

words = ["Green", "Grass"]
result = " ".join(words)
print(result)

#List concatenation [+, extend()]
list1 = [1,2,3]
list2 = [4,5,6]
result = list1 + list2
print(result)
list1.extend(list2)
print(list1)

#Tuple concatenation - homework
#Dictionary Concatenation [Python 3.9 and above,  |  and update() ]
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
result = dict1 | dict2
print(result)
dict1.update(dict2)
print(dict1)

#Set concatenation - homework

#( , ) comma operator - Separation
a = "Apple"
b = "Grapes"
print(a,b)
print("I am learning a programming language known as :","Python")
result = a,b
print(result)

firstname = "Tom"
lastname = "Alter"
print(firstname, lastname)
fullname = firstname,lastname
print(fullname)

list1 = [7,8,9]
list2 = [4,5,6]
result = list1+list2
print(result)

result_comma = [list1, list2]
print(result_comma)


