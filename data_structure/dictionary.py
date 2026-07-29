
student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A"
    }
print(student)  # Output: {'name': 'John Doe', 'age': 20, 'grade': 'A'}
print(student["name"])  # Output: John Doe
print(student["age"])   # Output: 20
print(student["grade"]) # Output: A
print(student.get("name"))  # Output: John Doe
print(student.get("age"))   # Output: 20
print(student.get("grade")) # Output: A
print(student.get("address", "Not Found"))  # Output: Not Found

student["age"] = 21  # Updating the age
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'grade': 'A'}

del student["grade"]  # Deleting the grade
print(student)  # Output: {'name': 'John Doe', 'age': 21}
