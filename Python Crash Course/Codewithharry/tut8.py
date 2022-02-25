

myvar = "Adnan is a good boy"
print(myvar[0:4]) 
#Even though Adnan is 0 to 4 but when we do 0:4 the 4 is not included so we need to write 0:5 so as to get the 4
print(myvar[0:5])
print(myvar[5]) #it printed the blank space between 'Adnan' and 'is'

#this thing is called *slicing*

print(len(myvar))
#output is 191
#Hence, Shows the length of the variable 0 to 18.
print(myvar[0:19])
#to get the whole output excluding 19.

print(myvar[0:483])
#It prints whatever it can from 0 and doesn't show error.

print(myvar[0:5:2])
#prints only 0, 2, 4 from 0 to 5.
"""The first colon indicates 'from' and the second indicates 'to' and the third indicates the space between them
It is always better to take the last colon as -1 and not any less than it.

IMPORTANT: Reversing the string or list does not change position values assigned to it. probably 
what I want to say is that Adnan will be 01234 and nandA will be 43210. probably"""

print(myvar[0:])
#prints till the end.

print(myvar[:5])
#includes the 0 automatically.

print(myvar[:])
#prints till the end.

print(myvar[::])
#prints 0 and 1 till the end.

print(myvar[::236472394])
#Runs throughout the print but couldn't find the letter pertaining to the input position so it just gives the 0

print(myvar[-1])
#-1 pertains to the last string/int

print(myvar[-3])
#prints only the 3rd last letter

print(myvar[-3:])
#print till third last 

print(myvar[::-1])
#prints from right to left.

print(myvar[-1:2:-1])
#First the code will go backwards then it will start with the last digit till positive 2 which will be 18 to 2 as -1 is 18
#Adn is 012 since the second colon excludes 2.
# from -1 to 1 since, it excludes 2. 

print(myvar[-1:-7:-1])
#The code is written in backwards due to last -1
#It will print from -1 to -6 and will exclude -7

print(myvar[::-2])
#reverse with the gap of 2 starting with -1

print(myvar[:-3])
# from -3 till 0 gets printed.





