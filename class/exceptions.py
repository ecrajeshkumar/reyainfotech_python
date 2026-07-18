
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution finished.") # finally → Always runs (cleanup, closing files, etc.).


# We can raise your own exceptions using raise.
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds!")
    return balance - amount

try:
    print(withdraw(1000, 1500))
except ValueError as e:
    print("Error:", e)

