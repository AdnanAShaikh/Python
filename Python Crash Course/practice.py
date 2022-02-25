#is and in are one of boolean operaters apart from ==, != , >=, =<, <, >, 

1 == 1
1 != 1

#name = input("My Name: ")
#input : 'Adnan'
#name == 'Falak'
#It will give me false as name was equals to Adnan
#the 'is' operator is similar to the equals to operator
#if I write name 'is' Adnan it will give true 

#the difference is that 'is' check not the values but the objects
#Eg:

#a = [1, 2, 4]
#b = [1, 2, 4]

#Here, the equals == will give true for a == b 
#but here the 'is' operator will give false as a and b are two different objects 

#The in operator check for the items included in the list
#3 in a will give False
#1 in a wil give true 

#_____________________________________________________________________________________

# THE 'not' keyword

#it is the opposite of 'is'

#a is b will give False
#a is not b will give true 

#____________________________________________________________________________________

# The 'and' and 'or data

#the and is used for checking 2 or more datas at the same time.
#it allows us to combine multiple conditions

age = 40
if age > 30 and age < 60:
    print("True as Age is 40 ")

# the 'or' operator is when you want to execute with either of the conditions.

if age > 10 or age > 20 or age == 40 or age < 50:
    print("I am really 40! not me though the age variable...")

#________________________________________________________________________________

# Combining grouping controls

# we can also combine and & or boolean operators.

name = 'LOL'
age = 18
if name == 'Adnan' and age > 30 or age == 18:
    print("True is it , is it not?")
#We get the condition as true even if the name didn't match WHy?
# Because Python sees Adnan and age > 30 as One condition
# and age == 18 as another condition
#Since, the first condition is wrong it goes for the second.

# also python here give preceedence to and over or.

name = 'LOL'
age = 18
if name == 'Adnan' and (age > 30 or age == 18):
    print("LOLOLOLOLOLOLOLOL")
else:
    print("NONONONONONONONONONONO")

