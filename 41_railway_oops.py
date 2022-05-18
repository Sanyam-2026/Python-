
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

SanyamsApplication = RailwayForm()
SanyamsApplication.name = "Sanyam"
SanyamsApplication.train = "Rajdhani Express"
SanyamsApplication.printData()