class Employee:
    company = "Google"
    salary = 100

Sanyam = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# Sanyam.salary = 300
# rajni.salary = 400
Sanyam.salary = 45
print(Sanyam.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 