
class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        self._balance +other._balance

    def display_details(self):
        return f"Account Holder: {self._name}, Balance: ₹{self._balance:.2f}"

class SavingsAccount(Account):
    def __init__(self, name, balance):
        Account.__init__(self, name, balance)

    def calculate_interest(self):
        return self._balance * 0.05
    
class CurrentAccount(Account):
    def __init__(self, name, balance):
        Account.__init__(self, name, balance)

    def calculate_interest(self):
        return self._balance * 0.02
    

savings_acc = SavingsAccount("Ravi", 10000)
current_acc = CurrentAccount("Anjali", 15000)

print(savings_acc.display_details())
print(f"Interest: ₹{savings_acc.calculate_interest():.2f}\n")

print(current_acc.display_details())
print(f"Interest: ₹{current_acc.calculate_interest():.2f}\n")

total_balance = savings_acc + current_acc
print(f"Total Balance (Ravi + Anjali): ₹{total_balance:.2f}")