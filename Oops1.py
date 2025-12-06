#initiate a class
class Employee:
    #initialize the class with ID and salary attributes
    def __init__(self):
        self.id = 231
        self.salary = 50000
        self.designation = "SDE"
    #Question- what is the speciality of the constructor method __init__()?
    #Answer: The __init__() method INITIATE the all things inside it as soon as we call the object.
    #Why is need of it : we need some of things to initialize automatically not the user have to do it manually.

    def travel(self, destination):
        print(f"Employee is traveling to {destination}")

# create an object of the Employee class
Arman = Employee()
print("ID:", Arman.id)
print("Salary:", Arman.salary)
print("Designation:", Arman.designation)
#calling a method using the object
Arman.travel("delhi")



