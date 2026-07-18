class Demo:
    def __init__(self):
        self.value = 10
        self._hidden = 20
        self.__secret = 30

    # Normal method
    def show_info(self):
        print(f"Demo class → value={self.value}, _hidden={self._hidden}, __secret={self._Demo__secret}")

    # Method to demonstrate behavior
    def greet(self):
        print("Hello from Demo class!")

class Derived(Demo):
    def __init__(self):
        super().__init__()
        self.value = 100
        self._hidden = 200
        self.__secret = 300

    # Overriding method
    def show_info(self):
        print(f"Derived class → value={self.value}, _hidden={self._hidden}, __secret={self._Derived__secret}")

    # Overriding greet method
    def greet(self):
        print("Hello from Derived class!")

    # New method only in Derived
    def show_parent_secret(self):
        print(f"Accessing parent secret: {self._Demo__secret}")

# Usage
obj1 = Demo()
obj1.show_info()   # Demo class → value=10, _hidden=20, __secret=30
obj1.greet()       # Hello from Demo class!

obj2 = Derived()
obj2.show_info()   # Derived class → value=100, _hidden=200, __secret=300
obj2.greet()       # Hello from Derived class!
obj2.show_parent_secret()  # Accessing parent secret: 30
