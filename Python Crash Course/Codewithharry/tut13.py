# IF and ELSE statements.
"""print("What is your age?")
age = int(input("Your Age: "))


#age should be 7 to 18 no drive. 18 will be please visit and greater than 18 and equal to 100 is eligible. any other integer is invalid.

if 7 < age < 18:
    print("Not eligible.")
elif age == 18:
    print("Please Visit")
elif 18<age<101:
    print("Eligible")
else:
    print("Invalid Age.")



"""



#college form : 
# if v1 yes v2 yes and age equal or greater than 18 then YES
# if v1 no v2 no and age less than 18 and consent form yes then YES
# if v1 yes and v2 no and age = or greater than 18 then NO

"""
def collegeform():
    v1 = int(input("Enter v1 status: "))
    v2 = int(input("Enter v2 status: "))
    consent_form = int(input("Enter consent form status: "))
    age = int(input("Enter your age: "))
    

    

    if v1 == 1 and v2  ==1 and consent_form ==1 and age >= 18:
        print("1.YEs")
    elif v1 == 0 and v2 == 0 and consent_form == 1 and age < 18:
        print("2.YEs")
    elif v1 == 1 and v2 == 0 and consent_form == 1 and age >= 18:
        print("3.Yes")
    else:
        print("4.NO")
    
  


collegeform()
    

   """


# Man opus entry

#Check for registered in book.
#Check for registered in app.
#For vehicles check ticket.
#If man opus but no ticket give ticket
#IF not man opus send them away. 
# IF delivery then contact. if yes then take if no then send away





