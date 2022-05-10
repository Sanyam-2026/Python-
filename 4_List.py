# a={"Sanyam",456,456.5676887}
from operator import indexOf


a=["Sanyam Jain", 7566029864,"sanyamjain6667@gmail.com","RNT Hostel "]

print(a)
print(type(a))

b= list(a)
print(type(b))
print(b)
#   Appending 
b.append(26)
print(b)

#  Inserting
b.insert(1,"Jain")
print(b)

#        Printing Details
print("Name : ", a[0] )
print("Contact Number  : ", a[1] )
print("Email  : ", a[2] )
print("Address  : ", a[3] )

for i in range(len(a)):
    print(a[i])

print(indexOf(a,"Sanyam Jain"))
print(indexOf(a,7566029864))