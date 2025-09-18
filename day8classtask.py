
class person:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def show_details(self):
        print(f"Person Name: {self.n}, Age: {self.a}")

class employee(person):
    def __init__(self,name,age,employee_id):
        person.__init__(self,name,age)
        self.id=employee_id

    def show_details(self):
        print(f"Employee Name: {self.n}, Age: {self.a}, Employee ID: {self.id}")

class part_time(person):
    def __init__(self,name,age,working_hours):
        person.__init__(self,name,age)
        self.hours=working_hours

    def show_details(self):
        print(f"Part-time workers Name: {self.n}, Age: {self.a}, Hours Worked: {self.hours}")

class consultant(employee,part_time):
    def __init__(self,name,age,employee_id,working_hours,project_name):
        employee.__init__(self,name,age,employee_id)
        part_time.__init__(self,name,age,working_hours)
        self.prjname=project_name

    def show_details(self):
        print(f"Consultant Name: {self.n}, Age: {self.a}, Employee ID: {self.id}, Hours Worked: {self.hours}, Project name: {self.prjname}")

p1 = person("Nervi", 20)
e1 = employee("Riya", 35, "E123")
pt1 = part_time("Meenu", 22, 25.5)
c1 = consultant("Afra", 30, "D702", 20.0, "Website Development")

p1.show_details()
e1.show_details()
pt1.show_details()
c1.show_details()