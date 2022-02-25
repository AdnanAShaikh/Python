a = [1, 2, 4, 3, 5, 9, 8]
#print(a[1:4])
#print(a[::-1])
#print(max(a))
#print(min(a))
#a.sort() in ascending order
#a.reverse()
#print(a.append(133))#Adds value at the end of a list.
#print(a.insert(1, 200)) #Adds value at a specfic position. insert(where, what)
#a.remove(2) #needs only one argument
#print(a.replace())
#a.pop()
#a.pop() 
#print(a)

#tuple = (1, 2, 3)
#print(tuple)
#print(tuple.append(4))

#In a tuple we cannot add or remove any elements in the parenthesis. 
#In a list we can add or remove any elements in the square brackets.

#MUTABLE -  list in which value can be added or subtracted eg: List[]
#IMMUTABLE - list in which value cannot be added nor subtracted eg: tuple()


c = 1
b = 3

#c, b = b, c
#print(c, b) #the values got interchanged.

temp = c
c = b
b = temp

print(c, b)# a more traditional way to change the values

