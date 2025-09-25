
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joinyear):
        self.__name = name
        self.__joinyear = joinyear

    def calculate_year(self):
        current_year = 2025
        return current_year - self.__joinyear
    def get_name(self):
        return self.__name
    
    @abstractmethod
    def role(self):
        pass

    def display_details(self):
        return f"Name: {self.__name}, - Role: {self.role()}, - Years of Service: {self.calculate_year()}"
    
class Customer(User):
    def role(self):
        return "Customer"
    
class Vendor(User):
    def role(self):
        return "Vendor"
    
Customer1=Customer("Riya", 2010)
Vendor1=Vendor("Amit", 2015)

print(Customer1.display_details())
print(Vendor1.display_details())
