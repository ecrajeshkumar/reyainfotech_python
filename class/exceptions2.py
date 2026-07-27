'''

Python provides four main keywords for handling exceptions: try, except, else and finally each plays a unique role. 
Let's see syntax:

try:
      # Code 
except SomeException:
      # Code 
else:
     # Code 
finally:
    # Code 

try: Runs the risky code that might cause an error.
except: Catches and handles the error if one occurs.
else: Executes only if no exception occurs in try.
finally: Runs regardless of what happens useful for cleanup tasks like closing files.

'''

try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")