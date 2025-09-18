
class Employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def display(self):
        print(f"Employee Name: {self.name}, Role: {self.role}")

class Trainer(Employee):
    def __init__(self,name,role,specialization):
        Employee.__init__(self,name,role)
        self.specialization=specialization
    def display(self):
        print(f"Trainer Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}")

class YogaInstructor(Employee):
    def __init__(self,name,role,yoga_style):
        Employee.__init__(self,name,role)
        self.yoga_style=yoga_style
    def display(self):
        print(f"Yoga Instructor Name: {self.name}, Role: {self.role}, Yoga Style: {self.yoga_style}")

class MultiTrainer(Trainer,YogaInstructor):
    def __init__(self,name,role,specialization,yoga_style):
        Trainer.__init__(self,name,role,specialization)
        YogaInstructor.__init__(self,name,role,yoga_style)
    def display(self):
        print(f"MultiTrainer Name: {self.name}, Role: {self.role}, Specialization: {self.specialization}, Yoga Style: {self.yoga_style}")


e1=Employee("Neethu","Manager")
t1=Trainer("Asha","Trainer","Cardio")
y1=YogaInstructor("Maya","Yoga Instructor","Yin")
m1=MultiTrainer("Lina","MultiTrainer","Strength","Hatha")

e1.display()
t1.display()
y1.display()
m1.display()