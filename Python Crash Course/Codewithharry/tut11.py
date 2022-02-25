#SETS in Python.

s = set()
#print(type(s))
#a = [2020, 2021, 2022, 2023, 2024, 2025]
#s_from_list = set([100, 200, 400, 600, 700])
#print(s_from_list)
#print(set([1, 2, 4, 6, 7]))
#print(set(a))

#s.add(1)
#s.add(1)
#print(s) 
''''Even though we added the int(1) 2 times when we printed we got only 1 times 1 instead of 2 times 1.
This is the main difference between sets and lists, Sets prints out unique value and ignore the repeated ones.
List prints whatever is in the list whether repeated or unrepeated.'''


s.add(2)
s.add(3)
print(s)
s1 = s.intersection([1, 2])
print(s1, s)  #Since 2 is the element both in s and s1. 
s2 = s.union([ 3, 4, 5])
print(s2, s) # Here s2 was 3, 4, 5 but it was with union with s = [2,3]
s3 = ([11, 12,13, 14, 15])
print(s1.isdisjoint(s3)) #Disjoint as the elements of s3 are not there in s.

s3.remove(11)
print(s3)

s3.insert(2, 24) #at 2nd position we want 24.
print(s3)# WE got it [12, 13, 24, 14, 15]


