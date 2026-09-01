# object oriented programming
# class,object,encapsilation,polymorphism
#inheritance , abstraction

#
# class : class is a blue print 
# Objects
# creating the calss and object
class Madam:
    # creating a consistor
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def student_details(self):
        print(f'hi {self.name},your roll number is{self.roll_no}')

    def ece (self):
        print("ece")
    def cse(self):
        print("computer")
# calling the object of any method 
student =Madam("nandini",234)
student.ece()
student.student_details()

#

class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def start(self):
        print(f"{self.brand} {self.model} is starting")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping")


car = Vehicle("Toyota", "Camry", 2025)

car.start()
car.stop()
###
class room:
    def __init__ (self,beds,plates,bathromm):
        self.beds=beds
        self.plates=plates
        self.bathroom=bathromm
    def beds(self):
        print(f"bead bedore eleven o clook and it must sevven to eight of sleep")
