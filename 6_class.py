class cars:
    def __init__(self,bname,model,types):
        self.b_name = bname
        self.model = model
        self.types = types

car1 = cars("BMW","x3","SUV")

print(car1.bname)
print(car1.model)
print(car1.types)