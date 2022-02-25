#Dictionaries and it's function

d1 = {} #This is a dictionary 
# list is [] and tuple is () and dict is {}

#d1 = {"Adnan": "Burger", 120 : "Pizza", 110 : "Almond", "Keval" : "Gujurati"}
#print(d1)
#print(type(d1))

#Add:
#d1["Kalash"] = "UttarPradesh"
#print(d1)

#del d1["Adnan"]
#print(d1)


#Copy a list
#d2 ={}
#d2 = d1.copy() #items removed in d2 will not be removed in d1 as it is just a copy which doesn't affect the original.
#print(d2)

#Dictionary within a dictionary

d1 = {"Adnan": "Burger", 120 : "Pizza", 110 : "Almond", "Keval" : "Gujurati", "Sarvesh":{"M": 12, "E": 13, "N": 14}}
#print(d1)
#print(d1["Sarvesh"])
d1.update({"Pizza" : 2000}) #Adds in a list. More better way.
print(d1)


#Replace:
#d1[120] = "Pavnan"
#print(d1)


#print(d1.items())
##print(d1.keys())

