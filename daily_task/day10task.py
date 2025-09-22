
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, accountyear):
        self.__name = name
        self.__accountyear = accountyear

    def account_age(self):
        current_year = 2025
        return current_year - self.__accountyear

    def get_name(self):
        return self.__name
    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "Admin"
    
    def __str__(self):
        return f"Name: {self.get_name()}, Role: {self.get_role()}, Account Age: {self.account_age()} years"
    
class Guest(User):
    def get_role(self):
        return "Guest"
    
    def __str__(self):
        return f"Name: {self.get_name()}, Role: {self.get_role()}, Account Age: {self.account_age()} years"
    
admin1=Admin("Sonu", 2018)
guest1=Guest("Monu", 2022)

print(admin1.get_role())
print(admin1.account_age())
print(admin1)

print(guest1.get_role())
print(guest1.account_age())
print(guest1)