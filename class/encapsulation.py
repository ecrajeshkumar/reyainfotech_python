# Encapsulation hides internal details and exposes only what’s necessary.
# In Python, we use private attributes (convention: prefix with _ or __).

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner         # This creates a public attribute. You can freely access and modify it outside the class:
        self.__balance = balance   # private

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

account = BankAccount("Rajesh", 1000)
account.deposit(500)
print(account.get_balance())   # Output: 1500

print(account.owner)        # ✅ Works its public data member
account.owner = "Punam"     # ✅ Can change directly
print(account.owner)        # Output: Punam

# - The double underscore (`__`) makes it a **private attribute** (name mangling).
# - Python internally renames it to `_ClassName__balance`, so direct access is discouraged:
# print(account.__balance)    # ❌ Error: Attribute not accessible directly
print(account._BankAccount__balance)  # ⚠️ Works, but not recommended

